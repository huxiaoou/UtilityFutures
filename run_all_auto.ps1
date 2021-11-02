$trade_date = Get-Date
$stp_date = $trade_date.AddDays(1)
$trade_date = $trade_date.ToString("yyyyMMdd")
$stp_date = $stp_date.ToString("yyyyMMdd")
Write-host "trade_date = " $trade_date
Write-host "stop_date  = " $stp_date
python run_all.py $stp_date >> .\log\$trade_date.log
