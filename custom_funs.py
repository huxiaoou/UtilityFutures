import numpy as np
import pandas as pd

MONTH_PER_YEAR = 12


def cal_major_return(x: pd.Series, t_this_prc_lbl: str, t_prev_prc_lbl: str, t_rtn_scale: float) -> float:
    res = x[t_this_prc_lbl] / x[t_prev_prc_lbl] - 1
    if np.isnan(res):
        return 0
    else:
        return np.round(res * t_rtn_scale, 8)


def czc_contract_id_expand(x: str, t_instru_id_len: int, t_trade_year: str) -> str:
    # x has a format like "MA105", in which "05" = May, however "1" is ambiguous, since it could be either "2011" or "2021"
    # this function is designed to solve this problem
    td = int(t_trade_year[2])  # decimal year to be inserted, "X" in "20XY"
    ty = int(t_trade_year[3])  # trade year number, "Y" in "20XY"
    cy = int(x[t_instru_id_len])  # contract year, "1" in "MA105"
    if cy < ty:
        # contract year should always be greater than or equal to the trade year
        # if not, decimal year +=1
        td += 1
    return x[0:t_instru_id_len] + str(td) + x[t_instru_id_len:]


def czc_contract_id_recover(x, t_instru_id_len) -> str:
    return x[0:t_instru_id_len] + x[(t_instru_id_len + 1):]
