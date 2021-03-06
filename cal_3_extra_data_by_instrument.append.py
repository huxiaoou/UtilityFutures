from setup import *
from skyrim.whiterun import CCalendar

'''
created @ 2022-01-17
0.  this script will reorganize extra data from by-date to by-instrument
'''

STP_DATE = sys.argv[1].upper()

calendar_cne = CCalendar(os.path.join(CALENDAR_DIR, "cne_calendar.csv"))

for extra_data_type in ["registered_stock", "basis"]:
    by_trade_date_dfs_list = []
    for trade_date in calendar_cne.get_iter_list(
            t_bgn_date=(dt.datetime.now() - dt.timedelta(days=20)).strftime("%Y%m%d"),
            t_stp_date=STP_DATE, t_ascending=True):
        src_file = "{}.cnf.{}.csv.gz".format(trade_date, extra_data_type)
        src_path = os.path.join(FUTURES_INSTRUMENT_MKT_DATA_DIR, trade_date[0:4], trade_date, src_file)
        if not os.path.exists(src_path):
            print("| Warning | {} data for {} does not exist".format(trade_date, extra_data_type))
            continue

        src_df = pd.read_csv(src_path, dtype="str")
        src_df["trade_date"] = trade_date
        by_trade_date_dfs_list.append(src_df)

    df: pd.DataFrame = pd.concat(by_trade_date_dfs_list, axis=0, ignore_index=True)
    for instrument, instrument_df in df.groupby(by="instrument"):
        if instrument in ["BC.INE"]:
            continue

        sorted_instrument_df = instrument_df.sort_values(by="trade_date").drop(labels="instrument", axis=1)

        instrument_file = "{}.{}.csv.gz".format(instrument, extra_data_type)
        instrument_path = os.path.join(EXTRA_DATA_DIR, instrument_file)
        old_sorted_instrument_df = pd.read_csv(instrument_path, dtype=str)

        new_sorted_instrument_df = pd.concat([
            old_sorted_instrument_df,
            sorted_instrument_df
        ]).drop_duplicates(keep="first")

        print("size before update:{}".format(len(old_sorted_instrument_df)))
        print("size after  update:{}".format(len(new_sorted_instrument_df)))
        print(old_sorted_instrument_df.tail())
        print(new_sorted_instrument_df.tail())

        new_sorted_instrument_df = new_sorted_instrument_df.sort_values("trade_date", ascending=True)
        new_sorted_instrument_df = new_sorted_instrument_df.set_index("trade_date")
        new_sorted_instrument_df.to_csv(instrument_path, index_label="trade_date")

        print("| {} | extra data {:>18s} for {:>6s} are updated".format(dt.datetime.now(), extra_data_type, instrument))
