"""
created @ 2021-02-03
0.  this project is designed to calculate some frequently used basic data for futures
"""

BGN_DATE, STP_DATE = "20120101", "20211011"
SIMU_BGN_DATE, SIMU_STP_DATE = "20150101", STP_DATE

# universe
CONCERNED_INSTRUMENT_UNIVERSE = [
    "CU.SHF",  # "19950417"
    "AL.SHF",  # "19950417"
    "PB.SHF",  # "20140801"
    "ZN.SHF",  # "20070326"
    "SN.SHF",  # "20151102"
    "NI.SHF",  # "20150327"
    "RB.SHF",  # "20090327"
    "HC.SHF",  # "20140321"
    "RU.SHF",  # "19950516"
    "BU.SHF",  # "20131009"

    "M.DCE",  # "20000717"
    "Y.DCE",  # "20060109"
    "A.DCE",  # "19990104"
    "P.DCE",  # "20071029"
    "C.DCE",  # "20040922"
    "CS.DCE",  # "20141219"
    "L.DCE",  # "20070731"
    "V.DCE",  # "20090525"
    "PP.DCE",  # "20140228"
    "J.DCE",  # "20110415"
    "JM.DCE",  # "20130322"
    "I.DCE",  # "20131018"

    "SR.CZC",  # "20060106"
    "CF.CZC",  # "20040601"
    "ZC.CZC",  # "20151201"
    "FG.CZC",  # "20121203"
    "TA.CZC",  # "20061218"
    "MA.CZC",  # "20141224"
    "OI.CZC",  # "20130423"
    "RM.CZC",  # "20121228"
]
CIU_SIZE = len(CONCERNED_INSTRUMENT_UNIVERSE)  # should be 30

# major
VOLUME_MOVING_AVER_N = 3

# misc
RETURN_SCALE = 100
