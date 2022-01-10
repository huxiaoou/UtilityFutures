$trade_date = Get-Date
$stp_date = $trade_date.AddDays(1)
$trade_date = $trade_date.ToString("yyyyMMdd")
$stp_date = $stp_date.ToString("yyyyMMdd")
Write-host "trade_date = " $trade_date
Write-host "stop_date  = " $stp_date
#python run_all.py $stp_date >> .\log\$trade_date.log
python cal_0_major_minor.py AU.SHF $stp_date >> .\log\$trade_date.log
python cal_1_major_return.py AU.SHF >> .\log\$trade_date.log
python cal_2_reformat_md.py AU.SHF $stp_date >> .\log\$trade_date.log
python cal_0_major_minor.py AG.SHF $stp_date >> .\log\$trade_date.log
python cal_1_major_return.py AG.SHF >> .\log\$trade_date.log
python cal_2_reformat_md.py AG.SHF $stp_date >> .\log\$trade_date.log
python cal_0_major_minor.py CU.SHF $stp_date >> .\log\$trade_date.log
python cal_1_major_return.py CU.SHF >> .\log\$trade_date.log
python cal_2_reformat_md.py CU.SHF $stp_date >> .\log\$trade_date.log
python cal_0_major_minor.py AL.SHF $stp_date >> .\log\$trade_date.log
python cal_1_major_return.py AL.SHF >> .\log\$trade_date.log
python cal_2_reformat_md.py AL.SHF $stp_date >> .\log\$trade_date.log
python cal_0_major_minor.py PB.SHF $stp_date >> .\log\$trade_date.log
python cal_1_major_return.py PB.SHF >> .\log\$trade_date.log
python cal_2_reformat_md.py PB.SHF $stp_date >> .\log\$trade_date.log
python cal_0_major_minor.py ZN.SHF $stp_date >> .\log\$trade_date.log
python cal_1_major_return.py ZN.SHF >> .\log\$trade_date.log
python cal_2_reformat_md.py ZN.SHF $stp_date >> .\log\$trade_date.log
python cal_0_major_minor.py SN.SHF $stp_date >> .\log\$trade_date.log
python cal_1_major_return.py SN.SHF >> .\log\$trade_date.log
python cal_2_reformat_md.py SN.SHF $stp_date >> .\log\$trade_date.log
python cal_0_major_minor.py NI.SHF $stp_date >> .\log\$trade_date.log
python cal_1_major_return.py NI.SHF >> .\log\$trade_date.log
python cal_2_reformat_md.py NI.SHF $stp_date >> .\log\$trade_date.log
python cal_0_major_minor.py RB.SHF $stp_date >> .\log\$trade_date.log
python cal_1_major_return.py RB.SHF >> .\log\$trade_date.log
python cal_2_reformat_md.py RB.SHF $stp_date >> .\log\$trade_date.log
python cal_0_major_minor.py HC.SHF $stp_date >> .\log\$trade_date.log
python cal_1_major_return.py HC.SHF >> .\log\$trade_date.log
python cal_2_reformat_md.py HC.SHF $stp_date >> .\log\$trade_date.log
python cal_0_major_minor.py RU.SHF $stp_date >> .\log\$trade_date.log
python cal_1_major_return.py RU.SHF >> .\log\$trade_date.log
python cal_2_reformat_md.py RU.SHF $stp_date >> .\log\$trade_date.log
python cal_0_major_minor.py BU.SHF $stp_date >> .\log\$trade_date.log
python cal_1_major_return.py BU.SHF >> .\log\$trade_date.log
python cal_2_reformat_md.py BU.SHF $stp_date >> .\log\$trade_date.log
python cal_0_major_minor.py FU.SHF $stp_date >> .\log\$trade_date.log
python cal_1_major_return.py FU.SHF >> .\log\$trade_date.log
python cal_2_reformat_md.py FU.SHF $stp_date >> .\log\$trade_date.log
python cal_0_major_minor.py SP.SHF $stp_date >> .\log\$trade_date.log
python cal_1_major_return.py SP.SHF >> .\log\$trade_date.log
python cal_2_reformat_md.py SP.SHF $stp_date >> .\log\$trade_date.log
python cal_0_major_minor.py SS.SHF $stp_date >> .\log\$trade_date.log
python cal_1_major_return.py SS.SHF >> .\log\$trade_date.log
python cal_2_reformat_md.py SS.SHF $stp_date >> .\log\$trade_date.log
python cal_0_major_minor.py M.DCE $stp_date >> .\log\$trade_date.log
python cal_1_major_return.py M.DCE >> .\log\$trade_date.log
python cal_2_reformat_md.py M.DCE $stp_date >> .\log\$trade_date.log
python cal_0_major_minor.py Y.DCE $stp_date >> .\log\$trade_date.log
python cal_1_major_return.py Y.DCE >> .\log\$trade_date.log
python cal_2_reformat_md.py Y.DCE $stp_date >> .\log\$trade_date.log
python cal_0_major_minor.py A.DCE $stp_date >> .\log\$trade_date.log
python cal_1_major_return.py A.DCE >> .\log\$trade_date.log
python cal_2_reformat_md.py A.DCE $stp_date >> .\log\$trade_date.log
python cal_0_major_minor.py P.DCE $stp_date >> .\log\$trade_date.log
python cal_1_major_return.py P.DCE >> .\log\$trade_date.log
python cal_2_reformat_md.py P.DCE $stp_date >> .\log\$trade_date.log
python cal_0_major_minor.py C.DCE $stp_date >> .\log\$trade_date.log
python cal_1_major_return.py C.DCE >> .\log\$trade_date.log
python cal_2_reformat_md.py C.DCE $stp_date >> .\log\$trade_date.log
python cal_0_major_minor.py CS.DCE $stp_date >> .\log\$trade_date.log
python cal_1_major_return.py CS.DCE >> .\log\$trade_date.log
python cal_2_reformat_md.py CS.DCE $stp_date >> .\log\$trade_date.log
python cal_0_major_minor.py L.DCE $stp_date >> .\log\$trade_date.log
python cal_1_major_return.py L.DCE >> .\log\$trade_date.log
python cal_2_reformat_md.py L.DCE $stp_date >> .\log\$trade_date.log
python cal_0_major_minor.py V.DCE $stp_date >> .\log\$trade_date.log
python cal_1_major_return.py V.DCE >> .\log\$trade_date.log
python cal_2_reformat_md.py V.DCE $stp_date >> .\log\$trade_date.log
python cal_0_major_minor.py PP.DCE $stp_date >> .\log\$trade_date.log
python cal_1_major_return.py PP.DCE >> .\log\$trade_date.log
python cal_2_reformat_md.py PP.DCE $stp_date >> .\log\$trade_date.log
python cal_0_major_minor.py EG.DCE $stp_date >> .\log\$trade_date.log
python cal_1_major_return.py EG.DCE >> .\log\$trade_date.log
python cal_2_reformat_md.py EG.DCE $stp_date >> .\log\$trade_date.log
python cal_0_major_minor.py EB.DCE $stp_date >> .\log\$trade_date.log
python cal_1_major_return.py EB.DCE >> .\log\$trade_date.log
python cal_2_reformat_md.py EB.DCE $stp_date >> .\log\$trade_date.log
python cal_0_major_minor.py PG.DCE $stp_date >> .\log\$trade_date.log
python cal_1_major_return.py PG.DCE >> .\log\$trade_date.log
python cal_2_reformat_md.py PG.DCE $stp_date >> .\log\$trade_date.log
python cal_0_major_minor.py J.DCE $stp_date >> .\log\$trade_date.log
python cal_1_major_return.py J.DCE >> .\log\$trade_date.log
python cal_2_reformat_md.py J.DCE $stp_date >> .\log\$trade_date.log
python cal_0_major_minor.py JM.DCE $stp_date >> .\log\$trade_date.log
python cal_1_major_return.py JM.DCE >> .\log\$trade_date.log
python cal_2_reformat_md.py JM.DCE $stp_date >> .\log\$trade_date.log
python cal_0_major_minor.py I.DCE $stp_date >> .\log\$trade_date.log
python cal_1_major_return.py I.DCE >> .\log\$trade_date.log
python cal_2_reformat_md.py I.DCE $stp_date >> .\log\$trade_date.log
python cal_0_major_minor.py JD.DCE $stp_date >> .\log\$trade_date.log
python cal_1_major_return.py JD.DCE >> .\log\$trade_date.log
python cal_2_reformat_md.py JD.DCE $stp_date >> .\log\$trade_date.log
python cal_0_major_minor.py RR.DCE $stp_date >> .\log\$trade_date.log
python cal_1_major_return.py RR.DCE >> .\log\$trade_date.log
python cal_2_reformat_md.py RR.DCE $stp_date >> .\log\$trade_date.log
python cal_0_major_minor.py SR.CZC $stp_date >> .\log\$trade_date.log
python cal_1_major_return.py SR.CZC >> .\log\$trade_date.log
python cal_2_reformat_md.py SR.CZC $stp_date >> .\log\$trade_date.log
python cal_0_major_minor.py CF.CZC $stp_date >> .\log\$trade_date.log
python cal_1_major_return.py CF.CZC >> .\log\$trade_date.log
python cal_2_reformat_md.py CF.CZC $stp_date >> .\log\$trade_date.log
python cal_0_major_minor.py CY.CZC $stp_date >> .\log\$trade_date.log
python cal_1_major_return.py CY.CZC >> .\log\$trade_date.log
python cal_2_reformat_md.py CY.CZC $stp_date >> .\log\$trade_date.log
python cal_0_major_minor.py AP.CZC $stp_date >> .\log\$trade_date.log
python cal_1_major_return.py AP.CZC >> .\log\$trade_date.log
python cal_2_reformat_md.py AP.CZC $stp_date >> .\log\$trade_date.log
python cal_0_major_minor.py CJ.CZC $stp_date >> .\log\$trade_date.log
python cal_1_major_return.py CJ.CZC >> .\log\$trade_date.log
python cal_2_reformat_md.py CJ.CZC $stp_date >> .\log\$trade_date.log
python cal_0_major_minor.py ZC.CZC $stp_date >> .\log\$trade_date.log
python cal_1_major_return.py ZC.CZC >> .\log\$trade_date.log
python cal_2_reformat_md.py ZC.CZC $stp_date >> .\log\$trade_date.log
python cal_0_major_minor.py FG.CZC $stp_date >> .\log\$trade_date.log
python cal_1_major_return.py FG.CZC >> .\log\$trade_date.log
python cal_2_reformat_md.py FG.CZC $stp_date >> .\log\$trade_date.log
python cal_0_major_minor.py SF.CZC $stp_date >> .\log\$trade_date.log
python cal_1_major_return.py SF.CZC >> .\log\$trade_date.log
python cal_2_reformat_md.py SF.CZC $stp_date >> .\log\$trade_date.log
python cal_0_major_minor.py SM.CZC $stp_date >> .\log\$trade_date.log
python cal_1_major_return.py SM.CZC >> .\log\$trade_date.log
python cal_2_reformat_md.py SM.CZC $stp_date >> .\log\$trade_date.log
python cal_0_major_minor.py TA.CZC $stp_date >> .\log\$trade_date.log
python cal_1_major_return.py TA.CZC >> .\log\$trade_date.log
python cal_2_reformat_md.py TA.CZC $stp_date >> .\log\$trade_date.log
python cal_0_major_minor.py MA.CZC $stp_date >> .\log\$trade_date.log
python cal_1_major_return.py MA.CZC >> .\log\$trade_date.log
python cal_2_reformat_md.py MA.CZC $stp_date >> .\log\$trade_date.log
python cal_0_major_minor.py UR.CZC $stp_date >> .\log\$trade_date.log
python cal_1_major_return.py UR.CZC >> .\log\$trade_date.log
python cal_2_reformat_md.py UR.CZC $stp_date >> .\log\$trade_date.log
python cal_0_major_minor.py SA.CZC $stp_date >> .\log\$trade_date.log
python cal_1_major_return.py SA.CZC >> .\log\$trade_date.log
python cal_2_reformat_md.py SA.CZC $stp_date >> .\log\$trade_date.log
python cal_0_major_minor.py OI.CZC $stp_date >> .\log\$trade_date.log
python cal_1_major_return.py OI.CZC >> .\log\$trade_date.log
python cal_2_reformat_md.py OI.CZC $stp_date >> .\log\$trade_date.log
python cal_0_major_minor.py RM.CZC $stp_date >> .\log\$trade_date.log
python cal_1_major_return.py RM.CZC >> .\log\$trade_date.log
python cal_2_reformat_md.py RM.CZC $stp_date >> .\log\$trade_date.log
