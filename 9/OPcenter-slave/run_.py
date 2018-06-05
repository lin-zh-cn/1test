#!/usr/bin/python3
# -*- coding: utf-8 -*-


import time
import requests
from requests.packages import urllib3
urllib3.disable_warnings()
from requests.exceptions import TooManyRedirects,ConnectionError,ReadTimeout

from requests.adapters import HTTPAdapter
from urllib3.exceptions import  LocationValueError
import json
from multiprocessing import Pool
# 导入配置文件
from config import *
from check_cert import Cert_check

import ssl
ssl._create_default_https_context = ssl._create_unverified_context
requests.packages.urllib3.disable_warnings()



def fault_post(domain_obj,event_type_id,cert_result):

    faultData = {
        'node': NODE,
        'url_id': domain_obj['id'],
        'domain': {
            'status_id': event_type_id,
            'cert_valid_date': cert_result['endDate'],
            'cert_valid_days': cert_result['expire']
        },
        'data': {
            'url_id': domain_obj['id'],
            'node_id': NODE,
            'datetime': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        },
        'event_log': {
            'event_type_id': event_type_id,
            'node_id': NODE,
            'url_id': domain_obj['id'],
            'datetime': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        }
    }
    print(faultData)
    fault_response = requests.post("http://" + SERVER + ":" + PORT + "/webmoni/api/fault_domain/",
                                  data={'faultData': json.dumps(faultData)})
    if fault_response.text != 'OK':
        print('失败域名提交时,API认证失败',fault_response.text)
        exit()

# 域名检测
def checkDomain(domain_obj,check_number):
    # 拼接url

    url = 'https://' + domain_obj['url']
    # # url = 'https://' + 'www.tt589.net'
    # 提交请求
    # start_time = time.time()
    try:
        requests.adapters.DEFAULT_RETRIES = 5
        start_time = time.time()
        response = requests.get(url,timeout=10,verify=False)
        stop_time = time.time()
        total_time = int((stop_time - start_time) * 1000)
        normalData = {
            'node': NODE,
            'url_id': domain_obj['id'],
            'data': {
                # 获取HTTP状态码
                'http_code': response.status_code,
                # 获取传输的总时间
                'total_time': total_time,
                'datetime': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                'node_id': NODE,
                'url_id': domain_obj['id']
            },
            'domain': {
                'status_id': '100',
            }
        }
        normal_response = requests.post("http://" + SERVER + ":" + PORT + "/webmoni/api/normal_domain/",
                                        data={'normalData': json.dumps(normalData)})

        if normal_response.text == 'OK':
            return True
        else:
            print('正常数据提交失败',normal_response.text)
            return False

    except ReadTimeout as e:
        cert_check_obj = Cert_check(domain_obj['url'])
        cert_result = cert_check_obj.py_check()
        fault_post(domain_obj,3,cert_result)
        return False
    except LocationValueError as e:
        cert_check_obj = Cert_check(domain_obj['url'])
        cert_result = cert_check_obj.py_check()
        fault_post(domain_obj,4,cert_result)
        return False
    except TooManyRedirects as e:
        cert_check_obj = Cert_check(domain_obj['url'])
        cert_result = cert_check_obj.py_check()
        fault_post(domain_obj,5,cert_result)
        return False
    except ConnectionError as e:
        cert_check_obj = Cert_check(domain_obj['url'])
        cert_result = cert_check_obj.py_check()
        fault_post(domain_obj,99,cert_result)
        return False





def main():
    # 这里开始轮询
    while True:
        # 设定轮询间隔时间
        print('技能冷却')
        time_remaining = INTERVAL - time.time() % INTERVAL
        # 整点开始
        time.sleep(time_remaining)
        print('技能引导')
        # 发送API请求 获取所有域名对象,连接失败会重试3次,
        session = requests.Session()
        session.mount('http://', HTTPAdapter(max_retries=3))

        domain_all_response = session.post("http://"+ SERVER +":"+ PORT +"/webmoni/api/domain_all/", data={'node': NODE})
        # 重试3次依旧失败就发送邮件并写入错误日志,退出程序

        # 获取API返回的域名对象,放入检查域名的进程池检查
        domain_all = json.loads(domain_all_response.text)
        if domain_all['status'] == 'OK':
            # 创建进程池，进程数=THREAD_NUM，进程调用函数main，参数url_t
            pool = Pool(THREAD_NUM)
            for domain_obj in domain_all['data']:
                if domain_obj['check_id'] == 0:
                    pool.apply_async(func=checkDomain, args=(domain_obj,0,))
            # 终止创建子进程
            pool.close()
            # 等待所有子进程结束
            pool.join()
            print('技能释放')

if __name__ == '__main__':
    main()

