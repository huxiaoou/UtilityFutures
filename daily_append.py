from setup import *
from configure import CONCERNED_INSTRUMENT_UNIVERSE
from skyrim.whiterun import CCalendar

calendar_cne = CCalendar(os.path.join(CALENDAR_DIR, "cne_calendar.csv"))
end_date = sys.argv[1]
stp_date = calendar_cne.get_next_date(t_this_date=end_date, t_shift=1)
for instrument in CONCERNED_INSTRUMENT_UNIVERSE:
    print("=" * 120)
    subprocess.run(["python", "cal_0_major_minor.append.py", instrument, stp_date])
    print("-" * 120)
    subprocess.run(["python", "cal_1_major_return.append.py", instrument])
    print("-" * 120)
    subprocess.run(["python", "cal_2_reformat_md.append.py", instrument, stp_date])

subprocess.run(["python", "cal_3_extra_data_by_instrument.append.py", stp_date])
