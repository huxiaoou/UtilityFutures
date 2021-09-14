import subprocess
from configure import CONCERNED_INSTRUMENT_UNIVERSE

for instrument_id in CONCERNED_INSTRUMENT_UNIVERSE:
    subprocess.call(["python", "cal_0_major_minor.py", instrument_id])
    subprocess.call(["python", "cal_1_major_return.py", instrument_id])
    subprocess.call(["python", "cal_2_reformat_md.py", instrument_id])
