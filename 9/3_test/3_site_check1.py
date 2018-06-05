import os
import time
import pycurl
import requests
from requests.packages import urllib3
urllib3.disable_warnings()
from requests.exceptions import TooManyRedirects,ConnectionError,ReadTimeout

from requests.adapters import HTTPAdapter
from urllib3.exceptions import  LocationValueError
import json
from json import JSONDecodeError
import datetime
import re
import subprocess
import ssl
import socket
from multiprocessing import Pool
# 导入配置文件
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 域名检测
def checkDomain(domain_obj):
    # 拼接url
    url = 'https://' + domain_obj['url']
    # # url = 'https://' + 'www.tt589.net'
    # 提交请求
    # start_time = time.time()
    try:
        requests.adapters.DEFAULT_RETRIES = 5
        start_time = time.time()
        response = requests.get(url,timeout=10,verify=False)
        print(response)
        stop_time = time.time()
        total_time = int((stop_time - start_time) * 1000)

        normalData = {
            'domainname': domain_obj['url'],
            # 获取HTTP状态码
            'http_code': response.status_code,
            # 获取传输的总时间
            'total_time': total_time,
            'datetime': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            'url_id': domain_obj['id']
        }

        print(normalData)

    except Exception as e:
        print(e)
    except ReadTimeout as e:
        cert_result = get_cert(domain_obj)
        fault_post(domain_obj,3,cert_result)
        return False
    except LocationValueError as e:
        cert_result = get_cert(domain_obj)
        fault_post(domain_obj,4,cert_result)
        return False
    except TooManyRedirects as e:
        cert_result = get_cert(domain_obj)
        fault_post(domain_obj,5,cert_result)
        return False
    except ConnectionError as e:
        cert_result = get_cert(domain_obj)
        fault_post(domain_obj,99,cert_result)
        return False

#domain_obj = {'id':'1', 'url':'ju888.net'}
domain_obj = {'id':'1', 'url':'tr77.net'}

checkDomain(domain_obj)