#!/usr/bin/bash
#host=$1
host="iju888.net"
port=443
end_date=`openssl s_client -host $host -port $port -showcerts </dev/null 2>/dev/null | sed -n '/BEGIN CERTIFICATE/,/END CERT/p' | openssl x509 -text 2>/dev/null | sed -n 's/ *Not After : *//p'`
if [ -n "$end_date" ]
then
    end_date_seconds=`date '+%s' --date "$end_date"`
# date指令format字符串时间。
    now_seconds=`date '+%s'`
    echo $end_date_seconds
    echo "($end_date_seconds-$now_seconds)/24/3600" | bc
fi

Le_CertEndTimeStr=1527761933


$Le_CertEndTimeStr + 90*24*3600