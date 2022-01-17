import os
import sys
import numpy as np
import pandas as pd
import datetime as dt

DATABASE = os.path.join("E:\\", "Database")
CALENDAR_DIR = os.path.join(DATABASE, "Calendar")
FUTURES_DIR = os.path.join(DATABASE, "Futures")
FUTURES_INSTRUMENT_MKT_DATA_DIR = os.path.join(FUTURES_DIR, "instrument_mkt_data")
MAJOR_MINOR_DIR = os.path.join(FUTURES_DIR, "by_instrument", "major_minor")
MAJOR_RETURN_DIR = os.path.join(FUTURES_DIR, "by_instrument", "major_return")
MKT_IDX_DIR = os.path.join(FUTURES_DIR, "by_instrument", "index", "CUSTOM")
EXTRA_DATA_DIR = os.path.join(FUTURES_DIR, "by_instrument", "extra_data")

MD_DIR = os.path.join(FUTURES_DIR, "by_instrument", "md")

INSTRUMENT_BGN_DATE = {
    "AL.SHF": "19950417",
    "CU.SHF": "19950417",
    "RU.SHF": "19950516",
    "A.DCE": "19990104",
    "M.DCE": "20000717",
    "CF.CZC": "20040601",
    "FU.SHF": "20180801",  # "20040825",
    "C.DCE": "20040922",
    "B.DCE": "20041222",
    "SR.CZC": "20060106",
    "Y.DCE": "20060109",
    "TA.CZC": "20061218",
    "ZN.SHF": "20070326",
    "L.DCE": "20070731",
    "P.DCE": "20071029",
    "AU.SHF": "20080109",
    "RB.SHF": "20090327",
    "WR.SHF": "20090327",
    "V.DCE": "20090525",
    "PB.SHF": "20140801",  # "20110324",
    "J.DCE": "20110415",
    "PM.CZC": "20120117",
    "AG.SHF": "20120510",
    "OI.CZC": "20130423",  # "20120716"
    "RI.CZC": "20120724",
    "WH.CZC": "20120724",
    "FG.CZC": "20121203",
    "RM.CZC": "20121228",
    "RS.CZC": "20121228",
    "JM.DCE": "20130322",
    "BU.SHF": "20150401",  # "20131009",
    "I.DCE": "20131018",
    "JD.DCE": "20131108",
    "JR.CZC": "20131118",
    "BB.DCE": "20131206",
    "FB.DCE": "20131206",
    "PP.DCE": "20140228",
    "HC.SHF": "20140321",
    "MA.CZC": "20141224",  # "20140617",
    "LR.CZC": "20140708",
    "SF.CZC": "20170808",  # "20140808",
    "SM.CZC": "20170203",  # "20140808",
    "CS.DCE": "20141219",
    "NI.SHF": "20150327",
    "SN.SHF": "20151102",  # "20150327",
    "ZC.CZC": "20151201",  # "20150518",
    "CY.CZC": "20170818",
    "AP.CZC": "20171222",
    "SC.INE": "20180326",
    "SP.SHF": "20181127",
    "EG.DCE": "20181210",
    "CJ.CZC": "20190430",
    "UR.CZC": "20190809",
    "NR.INE": "20190812",
    "RR.DCE": "20190816",
    "SS.SHF": "20190925",
    "EB.DCE": "20190926",
    "SA.CZC": "20191206",
    "PG.DCE": "20200330",
}

'''
for instrument OI began at "20120716"
however, code has changed since "2013-07"
as the result of this, since 20130423, major and minor contracts are stable

for instrument MA began at "20140617"                              
however, code has changed since "2015-06", and contract multiplier reduced from 50 to 10 as well                                  
as the result of this, since "20141224", major and minor contracts are stable

for instrument ZC began at "20150518"                              
however, code has changed since "2016-05", and contract multiplier reduced from 200 to 100 as well                                  
as the result of this, since "20151201", major and minor contracts are stable

for instrument FU began at "20040825"                              
however, contract details have been revised, contract multiplier reduced from 50 to 10 as well                                  
as the result of this, since "20180801", major and minor contracts are stable

for instrument SF and SM, both began at "20140808"                              
however, daily volume have been very low since until year 2017. so "20170808" and "20170203" have been
set as the beginning for each separately

for instrument BU, began at "20131009"                              
however, daily volume have been very low since until year 2015. so "20150401" have been
set as the beginning for each separately

for instrument J,JM and I, minispread are changed since 2015-04-17 21:00
    J: 1->0.5
    JM: 1->0.5
    I: 1->0.5
'''
