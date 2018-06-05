# !/usr/bin/env python3

"""Show server's certificate as json.

Usage:
  $ %(prog)s HOST [PORT]
"""
import time
import datetime
import json
import socket
import ssl
import sys
from OpenSSL import SSL
from multiprocessing import Pool
from domains_all import  *

def getcert(addr, timeout=10):
    """Retrieve server's certificate at the specified address (host, port)."""
    # it is similar to ssl.get_server_certificate() but it returns a dict
    # and it verifies ssl unconditionally, assuming create_default_context does
    with socket.create_connection(addr, timeout=timeout) as sock:
        context = ssl.create_default_context()
        with context.wrap_socket(sock, server_hostname=addr[0]) as sslsock:
            return sslsock.getpeercert()

host = "ju11.net"
#host = "www.baidu.com"
port = 443
print(json.dumps(getcert((host, port)), indent=2, sort_keys=True))



"""
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
    
"""
