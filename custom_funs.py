import numpy as np
import pandas as pd

MONTH_PER_YEAR = 12


def cal_major_return(x: pd.Series, t_this_prc_lbl: str, t_prev_prc_lbl: str, t_rtn_scale: float) -> float:
    res = x[t_this_prc_lbl] / x[t_prev_prc_lbl] - 1
    if np.isnan(res):
        return 0
    else:
        return np.round(res * t_rtn_scale, 8)


def czc_contract_id_expand(x: str, t_instru_id_len: int, t_year: str) -> str:
    # x has a format like "MA905", in which "05" = May, however "9" is ambiguous, since it can be "2019" or "2009"
    # this function is designed to solve this problem
    d = int(t_year[2])  # decimal year to be insert, such as "1" in "2019" or second "0" in "2009"
    y = int(t_year[3])  # trade year number, "9" in "2019"
    cy = int(x[t_instru_id_len])  # contract year, "9" in "MA905"
    if cy < y:
        # contract year should always be greater than or equal to the trade year
        # if not, decimal year +=1
        d += 1
    return x[0:t_instru_id_len] + str(d) + x[t_instru_id_len:]


def czc_contract_id_recover(x, t_instru_id_len) -> str:
    return x[0:t_instru_id_len] + x[(t_instru_id_len + 1):]
