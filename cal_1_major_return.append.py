from setup import *
from configure import *
from custom_funs import cal_major_return

'''
created @ 2022-05-25
0.  update with increment mode  
'''

# --- basic settings
instrument_id = sys.argv[1].upper()
price_type = "close"
this_prc_lbl = "this_{}".format(price_type)
prev_prc_lbl = "prev_{}".format(price_type)
actual_bgn_date = max(INSTRUMENT_BGN_DATE[instrument_id], (dt.datetime.now() - dt.timedelta(days=30)).strftime("%Y%m%d"))

# --- load major table
input_file = "major.minor.{}.csv.gz".format(instrument_id)
input_path = os.path.join(MAJOR_MINOR_DIR, input_file)
input_df = pd.read_csv(input_path, dtype={"trade_date": str})
input_df["major_rtn_contract"] = input_df["n_contract"]
input_df[this_prc_lbl] = None
input_df[prev_prc_lbl] = None
input_df["volume"] = 0
input_df["amt"] = 0
input_df["oi"] = 0
input_df = input_df.set_index("trade_date")
input_df = input_df.loc[input_df.index >= actual_bgn_date]

# --- update price
prev_trade_date = None
prev_md_df = None
for this_trade_date in input_df.index:
    # print(this_trade_date)
    trade_year = this_trade_date[0:4]
    this_md_file = "{}.cnf.{}.md.csv.gz".format(this_trade_date, instrument_id)
    this_md_path = os.path.join(FUTURES_INSTRUMENT_MKT_DATA_DIR, this_trade_date[0:4], this_trade_date, this_md_file)
    this_md_df = pd.read_csv(this_md_path).set_index("contract")

    vo_adj_ratio = 2 if this_trade_date < "20200101" else 1

    m_contract = input_df.at[this_trade_date, "major_rtn_contract"]
    if m_contract in this_md_df.index:
        m_this_price = this_md_df.at[m_contract, price_type]
        m_this_volume = this_md_df.at[m_contract, "volume"] / vo_adj_ratio
        m_this_amt = 0 if np.isnan(this_md_df.at[m_contract, "amt"]) else this_md_df.at[m_contract, "amt"] / vo_adj_ratio
        m_this_oi = this_md_df.at[m_contract, "oi"] / vo_adj_ratio
    else:
        m_this_price = np.nan
        m_this_volume = 0
        m_this_amt = 0
        m_this_oi = 0

    if prev_md_df is not None:
        if m_contract in prev_md_df.index:
            m_prev_price = prev_md_df.at[m_contract, price_type]
        else:
            m_prev_price = np.nan
    else:
        m_prev_price = m_this_price
        print("| {} | {:>6s} | {} | prev date md missing    |".format(dt.datetime.now(), instrument_id, this_trade_date))

    input_df.at[this_trade_date, this_prc_lbl] = m_this_price
    input_df.at[this_trade_date, prev_prc_lbl] = m_prev_price
    input_df.at[this_trade_date, "volume"] = m_this_volume
    input_df.at[this_trade_date, "amt"] = m_this_amt
    input_df.at[this_trade_date, "oi"] = m_this_oi

    # for next day
    prev_md_df = this_md_df

# --- major return
input_df["major_return"] = input_df[[this_prc_lbl, prev_prc_lbl]].apply(
    cal_major_return, t_this_prc_lbl=this_prc_lbl, t_prev_prc_lbl=prev_prc_lbl, t_rtn_scale=RETURN_SCALE,
    axis=1
)
input_df = input_df.tail(len(input_df) - 1)  # drop first row, where the "major_return" is not correct

# --- load old
major_return_file = "major_return.{}.{}.csv.gz".format(instrument_id, price_type)
major_return_path = os.path.join(MAJOR_RETURN_DIR, major_return_file)
old_major_return_df = pd.read_csv(major_return_path, dtype={"trade_date": str})

# --- concat old and new
new_major_return_df = pd.concat([
    old_major_return_df.drop(labels=["mkt_idx"], axis=1),
    input_df.drop(labels=["d_contract"], axis=1).reset_index().rename(mapper={"index": "trade_date"}, axis=1)
])
new_major_return_df = new_major_return_df.drop_duplicates(keep="first").sort_values("trade_date", ascending=True)
new_major_return_df["mkt_idx"] = (new_major_return_df["major_return"] / RETURN_SCALE + 1).cumprod()

if instrument_id == "ZC.CZC":
    new_major_return_df = new_major_return_df.drop_duplicates(keep="last", subset=["trade_date"])

# --- reformat and save
print("size before update:{}".format(len(old_major_return_df)))
print("size after  update:{}".format(len(new_major_return_df)))
print(old_major_return_df.tail())
print(new_major_return_df.tail())

new_major_return_df = new_major_return_df.set_index("trade_date")
new_major_return_df = new_major_return_df[["n_contract", "major_rtn_contract", this_prc_lbl, prev_prc_lbl, "major_return", "volume", "amt", "oi", "mkt_idx"]]
new_major_return_df.to_csv(major_return_path, float_format="%.8f", compression="gzip")

# --- custom market return
custom_mkt_idx_df = new_major_return_df[["mkt_idx"]].rename(mapper={"mkt_idx": price_type.upper()}, axis=1)
custom_mkt_idx_file = "{}.index.csv.gz".format(instrument_id)
custom_mkt_idx_path = os.path.join(MKT_IDX_DIR, custom_mkt_idx_file)
custom_mkt_idx_df.to_csv(custom_mkt_idx_path, float_format="%.8f", compression="gzip")

print("| {} | {:>6s} | {:>8s} | Major return calculated |".format(dt.datetime.now(), instrument_id, price_type))
