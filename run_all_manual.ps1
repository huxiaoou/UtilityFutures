$trade_date = Read-Host -Prompt "Please input the stp date, format = [YYYYMMDDD]"
python run_all.py $trade_date >> .\log\$trade_date.log
