#!/usr/bin/bash
host=$1
port=443
end_date=`timeout 10 openssl s_client -host $host -port $port -showcerts </dev/null 2>/dev/null | sed -n '/BEGIN CERTIFICATE/,/END CERT/p' | openssl x509 -text 2>/dev/null | sed -n 's/ *Not After : *//p'`
if [ -n "$end_date" ]
then
    end_date_seconds=`date '+%s' --date "$end_date"`
# date指令format字符串时间。
    now_seconds=`date '+%s'`
    echo $host
    echo "($end_date_seconds-$now_seconds)/3600/24" | bc
fi