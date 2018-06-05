import socket
import ssl


def get_cert(hostname):
    try:
        ctx = ssl.create_default_context()
        s = ctx.wrap_socket(socket.socket(), server_hostname=hostname)
        s.settimeout(5)
        s.connect((hostname, 443))
        cert = s.getpeercert()
        # 有效期结束
        notAfter = cert['notAfter']
        notAfter = time.mktime(time.strptime(notAfter, '%b %d %H:%M:%S %Y %Z'))
        # 当前时间
        nowDate = time.time()
        # 时间差
        expire = (notAfter - nowDate) / 3600 / 24
        # 时间格式本地化
        endDate = time.strftime("%Y-%m-%d", time.localtime(notAfter))
        print("站点：%s \r\n证书有效期至%s," % (hostname, endDate), "还有%s天到期\r\n" % int(expire))

    except Exception as e:
        print(hostname,"\r\n",e,"\r\n")



