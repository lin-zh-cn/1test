import time
import ssl
import os
import socket
import OpenSSL
from multiprocessing import Pool
from domains_all import  *
import subprocess

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
        result = subprocess.getstatusoutput(os.path.dirname(os.path.realpath(__file__))+ '/openssl_check_cert.sh  ' + hostname)
        print(result)

if __name__ == '__main__':
    try:
        pool = Pool(10)
        for hostname in domains:
            pool.apply_async(func=get_cert, args=(hostname,))
        # 终止创建子进程
        pool.close()
        # 等待所有子进程结束
        pool.join()
    except Exception as e:
        print(e)
