import subprocess
import sys
from configure import CONCERNED_INSTRUMENT_UNIVERSE
from time import sleep

stp_date = sys.argv[1]

for instrument_id in CONCERNED_INSTRUMENT_UNIVERSE:
    sleep(1)
    subprocess.run(["python", "cal_0_major_minor.py", instrument_id, stp_date])
    sleep(1)
    subprocess.run(["python", "cal_1_major_return.py", instrument_id])
    sleep(1)
    subprocess.run(["python", "cal_2_reformat_md.py", instrument_id, stp_date])
