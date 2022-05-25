from setup import *
from configure import CONCERNED_INSTRUMENT_UNIVERSE

stp_date = sys.argv[1]
for instrument in CONCERNED_INSTRUMENT_UNIVERSE:
    # subprocess.run(["python", "cal_0_major_minor.append.py", instrument, stp_date])
    # subprocess.run(["python", "cal_1_major_return.append.py", instrument])
    # subprocess.run(["python", "cal_2_reformat_md.append.py", instrument, stp_date])
    pass

subprocess.run(["python", "cal_3_extra_data_by_instrument.append.py", stp_date])
