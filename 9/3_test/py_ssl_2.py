#!/usr/bin/env python
# coding:utf-8
import ssl
import socket
import os
from multiprocessing import Pool
from domains_all import  *

def Check_https(check_list):

    for url in check_list:




if __name__ == '__main__':

    check_list = ['www.baidu.com', 'www.chinassl.net']
    check = Check_https(check_list)



#hostname = 'www.baidu.com'
def get_cert(hostname):
        print(hostname)
        try:
            ctx = ssl.create_default_context()
            s = ctx.wrap_socket(socket.socket(), server_hostname=hostname)
            s.connect((hostname, 443))
            cert = s.getpeercert()

            subject = dict(x[0] for x in cert['subject'])
            issued_to = subject['commonName']
            issuer = dict(x[0] for x in cert['issuer'])
            issued_by = issuer['commonName']
            print(cert)
        except Exception as e:
            result = os.popen('sh test.sh {0}'.format(hostname))
            result = result.read().strip().split('\n')[-1]
            print(result)
            if result.isdigit():
                if int(result) > 0:
                    print("沒有過期")
                else:
                    print("國了")
                    send_email(result, to_list, 'hi 过期了')




        except Exception as e:
            print(e)
            with open('ssl_err_hostname.log', 'a+') as f:
                f.write("%s\r\n" % (hostname))
            f.close()

if __name__ == '__main__':
    try:
        pool = Pool(20)
        for hostname in domains:
            pool.apply_async(func=get_cert, args=(hostname,))
        # 终止创建子进程
        pool.close()
        # 等待所有子进程结束
        pool.join()
    except Exception as e:
        print(e)
