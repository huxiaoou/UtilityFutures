from setup import *
from configure import BGN_DATE
from skyrim.whiterun import CCalendar

'''
created @ 2022-01-17
0.  this script will reorganize extra data from by-date to by-instrument
'''

STP_DATE = sys.argv[1].upper()

calendar_cne = CCalendar(os.path.join(CALENDAR_DIR, "cne_calendar.csv"))

for extra_data_type in ["registered_stock", "basis"]:
    by_trade_date_dfs_list = []
    for trade_date in calendar_cne.get_iter_list(t_bgn_date=BGN_DATE, t_stp_date=STP_DATE, t_ascending=True):
        src_file = "{}.cnf.{}.csv.gz".format(trade_date, extra_data_type)
        src_path = os.path.join(FUTURES_INSTRUMENT_MKT_DATA_DIR, trade_date[0:4], trade_date, src_file)
        if not os.path.exists(src_path):
            continue

        src_df = pd.read_csv(src_path, dtype="str")
        src_df["trade_date"] = trade_date
        by_trade_date_dfs_list.append(src_df)

    df: pd.DataFrame = pd.concat(by_trade_date_dfs_list, axis=0, ignore_index=True)
    for instrument, instrument_df in df.groupby(by="instrument"):
        if instrument in ["BC.INE"]:
            continue

        sorted_instrument_df = instrument_df.sort_values(by="trade_date").drop(labels="instrument", axis=1).set_index("trade_date")
        instrument_file = "{}.{}.csv.gz".format(instrument, extra_data_type)
        instrument_path = os.path.join(EXTRA_DATA_DIR, instrument_file)
        sorted_instrument_df.to_csv(instrument_path, index_label="trade_date")

    print("... Extra data: {:>18s} by instrument calculated".format(extra_data_type))
