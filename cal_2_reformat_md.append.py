from setup import *
from configure import SIMU_BGN_DATE
from skyrim.whiterun import CCalendar

'''
created @ 2021-02-08
0.  DO NOT set the gap between the SIMU_BGN_DATE and SIMU_STP_DATE longer than 10 years, or
    this could be lead to some bugs due to the fucking-lazy contract id naming rule of CZC.
1.  the results of this script provide some basic input for precise daily simulation
'''

instrument_id = sys.argv[1].upper()
SIMU_STP_DATE = sys.argv[2]
exchange_id = instrument_id.split(".")[1]
instrument_id_len = len(instrument_id.split(".")[0])

for price_type in ["open", "close"]:
    # --- load
    actual_bgn_date = max(INSTRUMENT_BGN_DATE[instrument_id], (dt.datetime.now() - dt.timedelta(days=20)).strftime("%Y%m%d"))
    calendar_cne = CCalendar(os.path.join(CALENDAR_DIR, "cne_calendar.csv"))
    md_dfs_list = []
    for trade_date in calendar_cne.get_iter_list(t_bgn_date=actual_bgn_date, t_stp_date=SIMU_STP_DATE, t_ascending=True):
        trade_year = trade_date[0:4]
        instrument_md_file = "{}.cnf.{}.md.csv.gz".format(trade_date, instrument_id)
        instrument_md_path = os.path.join(FUTURES_INSTRUMENT_MKT_DATA_DIR, trade_date[0:4], trade_date, instrument_md_file)
        instrument_md_df = pd.read_csv(instrument_md_path)
        instrument_md_df["trade_date"] = trade_date
        instrument_md_df = instrument_md_df[["trade_date", "contract", price_type]]
        md_dfs_list.append(instrument_md_df)

    md_df = pd.concat(md_dfs_list, axis=0, ignore_index=True)
    price_df = pd.pivot_table(data=md_df, values=price_type, index="trade_date", columns="contract", dropna=False)

    # load old
    price_file = "{}.md.{}.csv.gz".format(instrument_id, price_type)
    price_path = os.path.join(MD_DIR, price_file)
    old_price_df = pd.read_csv(price_path, dtype={"trade_date": str})

    # concat
    new_price_df = pd.concat([
        old_price_df,
        price_df.reset_index().rename(mapper={"index": "trade_date"}, axis=1)
    ])
    new_price_df = new_price_df.drop_duplicates(keep="first").sort_values("trade_date", ascending=True)

    # print(old_price_df.tail())
    # print(new_price_df.tail())

    new_price_df = new_price_df.set_index("trade_date")
    new_price_df.to_csv(price_path, float_format="%.2f", compression="gzip")

    print("| {} | {:>6s} | {:>8s} | md reformat |".format(dt.datetime.now(), instrument_id, price_type))
