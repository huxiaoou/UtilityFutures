from setup import *
from custom_funs import czc_contract_id_recover, czc_contract_id_expand
from configure import VOLUME_MOVING_AVER_N
from skyrim.whiterun import CCalendar

'''
created @ 2022-05-25
0.  update with increment mode  
'''

instrument_id = sys.argv[1].upper()
STP_DATE = sys.argv[2]

exchange_id = instrument_id.split(".")[1]
instrument_id_len = len(instrument_id.split(".")[0])

actual_bgn_date = max(INSTRUMENT_BGN_DATE[instrument_id], (dt.datetime.now() - dt.timedelta(days=30)).strftime("%Y%m%d"))
calendar_cne = CCalendar(os.path.join(CALENDAR_DIR, "cne_calendar.csv"))
md_dfs_list = []
for trade_date in calendar_cne.get_iter_list(t_bgn_date=actual_bgn_date, t_stp_date=STP_DATE, t_ascending=True):
    trade_year = trade_date[0:4]
    instrument_md_file = "{}.cnf.{}.md.csv.gz".format(trade_date, instrument_id)
    instrument_md_path = os.path.join(FUTURES_INSTRUMENT_MKT_DATA_DIR, trade_date[0:4], trade_date, instrument_md_file)
    instrument_md_df = pd.read_csv(instrument_md_path)
    instrument_md_df["trade_date"] = trade_date
    instrument_md_df = instrument_md_df[["trade_date", "contract", "volume", "close", "open"]]
    if exchange_id == "CZC":
        instrument_md_df["contract"] = instrument_md_df["contract"].map(lambda x: czc_contract_id_expand(x, instrument_id_len, trade_year))
    md_dfs_list.append(instrument_md_df)

md_df = pd.concat(md_dfs_list, axis=0, ignore_index=True)
pivot_volume_df = pd.pivot_table(data=md_df, values="volume", index="trade_date", columns="contract").fillna(0)
pivot_volume_df_sorted = pivot_volume_df.sort_index(axis=1).sort_index(axis=0)
volume_mov_aver_df = pivot_volume_df_sorted.rolling(window=VOLUME_MOVING_AVER_N).mean()
volume_mov_aver_df = volume_mov_aver_df.shift(2)
volume_mov_aver_df = volume_mov_aver_df.tail(len(volume_mov_aver_df) - 2 - VOLUME_MOVING_AVER_N)  # drop first few rows, where the moving average volume is not correct

# main loop to get major and minor contracts
n_contract = pre_n_contract = None
d_contract = pre_d_contract = None
pre_trade_date = None
major_minor_data = {}
for trade_date in volume_mov_aver_df.index:
    # update near and distant contract
    t_oi_srs = volume_mov_aver_df.loc[trade_date]
    n_contract = t_oi_srs.idxmax()
    if n_contract.split(".")[0][-4:] < trade_date[2:6]:
        n_contract = pre_n_contract

    t_oi_srs_future = t_oi_srs[t_oi_srs.index > n_contract]
    if len(t_oi_srs_future) > 0:
        d_contract = t_oi_srs_future.idxmax()
    else:
        d_contract = n_contract

    # append to data
    major_minor_data[trade_date] = {
        "n_contract": n_contract,
        "d_contract": d_contract,
    }

    # for next trade date
    pre_trade_date = trade_date
    pre_n_contract = n_contract
    pre_d_contract = d_contract

major_minor_df = pd.DataFrame.from_dict(major_minor_data, orient="index")
if exchange_id == "CZC":
    major_minor_df["n_contract"] = major_minor_df["n_contract"].map(lambda x: czc_contract_id_recover(x, instrument_id_len))
    major_minor_df["d_contract"] = major_minor_df["d_contract"].map(lambda x: czc_contract_id_recover(x, instrument_id_len))

save_file = "major.minor.{}.csv.gz".format(instrument_id)
save_path = os.path.join(MAJOR_MINOR_DIR, save_file)

old_df = pd.read_csv(save_path, dtype=str)
save_df = pd.concat([old_df, major_minor_df.reset_index().rename(mapper={"index": "trade_date"}, axis=1)])
save_df = save_df.drop_duplicates(keep="first").sort_values("trade_date", ascending=True)
if instrument_id == "ZC.CZC":
    # added @ 2022-10-10
    # for ZC.CZC may have some duplicates due to few volume at nowadays.
    save_df = save_df.drop_duplicates(keep="last", subset=["trade_date"])

print("size before update:{}".format(len(old_df)))
print("size after  update:{}".format(len(save_df)))
print(old_df.tail())
print(save_df.tail())

save_df = save_df.set_index("trade_date")
save_df.to_csv(save_path, index_label="trade_date", compression="gzip")

print("| {} | {:>6s} | {} | {} | Major and Minor contracts calculated |".format(dt.datetime.now(), instrument_id, actual_bgn_date, STP_DATE))
