#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import time
import pycurl
import pymysql
import subprocess
from multiprocessing import Pool
# 导入配置文件
from config1 import *

# 记录日志
def write_log(e):
    # 异常出现时间
    err_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # 异常信息
    error_info = "[%s] %s\r\n" % (err_time, e)
    with open('error.log','a+') as f:
        try:
            f.write(error_info)
        finally:
            if f:
                f.close()

# 建立数据库连接
def db_connect():
    try:
        # 获取数据库
        conn = pymysql.connect(host=HOST, port=PORT, user=USER, passwd=PASSWORD, db=DB, charset='utf8')
        # 获得游标指针
        cursor = conn.cursor()
        # 函数返回值，供其他函数调用
        return conn,cursor
    except Exception as e:
        print("建立数据库连接出现异常")
        # 记录异常日志
        write_log(e)
        # 异常时等待重新连接
        time.sleep(RETRY)
        # 重新尝试建立连接
        return db_connect()

# 关闭数据库连接
def db_close(cursor,conn):
    try:
        # 关闭游标
        cursor.close()
        # 关闭连接
        conn.close()
    except Exception as e:
        print("关闭数据库连接出现异常")
        # 记录异常日志
        write_log(e)
        # 异常时等待重新连接
        time.sleep(RETRY)
        # 重新尝试关闭连接
        return db_close(cursor,conn)

# 获取异常事件类型id
def event_type(e):
    # 获取数据库连接和游标指针
    conn, cursor = db_connect()
    # 查询出所有事件类型event_types
    cursor.execute('select * from webmoni_event_type where (id != 0)')
    event_types = cursor.fetchall()
    db_close(cursor,conn)

    # 遍历匹配出类型id：event_type[0]，并作为函数结果返回
    for event_type in event_types:
        if event_type[1] in e:
            return event_type[0]
    # 没有匹配到的错误，则记录日志到
    else:
        # 记录新事件日志./event.log
        fo = open("event.log", "a+")
        err_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        fo.write("[%s] %s\r\n" % (err_time, e))
        fo.close()
        # 返回Unknown error的ID：99
        return 99

# 域名检测
def checkDomain(url_t,check_number):
    # 获得url
    url = 'https://' + url_t[1]
    #url = 'https://' + 'ju999.net'
    # 创建Curl对象
    c = pycurl.Curl()
    # 定义请求的URL
    c.setopt(pycurl.URL, url)
    # 设置证书
    # c.setopt(pycurl.SSL_VERIFYPEER, 1)
    # c.setopt(pycurl.SSL_VERIFYHOST, 2)
    # c.setopt(pycurl.CAINFO, certifi.where())
    # 忽略证书
    c.setopt(pycurl.SSL_VERIFYPEER, 0)
    c.setopt(pycurl.SSL_VERIFYHOST, 0)
    # 模拟IE11浏览器
    c.setopt(pycurl.USERAGENT,
             "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko")
    # 模拟Safari浏览器
    #c.setopt(pycurl.USERAGENT,
      #       "Mozilla/5.0(Macintosh;intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/52.0.2743.116 Safari/537.36")
    # 定义请求连接的等待时间
    c.setopt(pycurl.CONNECTTIMEOUT, TIME_OUT)
    # 定义请求超时时间
    c.setopt(pycurl.TIMEOUT, TIME_OUT)
    # 屏蔽下载进度条
    c.setopt(pycurl.NOPROGRESS, 1)
    # 完成交互后强制断开连接，不重用
    c.setopt(pycurl.FORBID_REUSE, 1)
    # 指定HTTP重定向的最大次数为10
    c.setopt(pycurl.MAXREDIRS, 5)
    # 设置保存DNS信息的时间
    c.setopt(pycurl.DNS_CACHE_TIMEOUT, 1)
    # 创建一个文件，以wb方式打开，用来存储返回的HTTP头部和页面内容
    indexFile = open(os.path.dirname(os.path.realpath(__file__)) + "content.txt", "wb")
    # 将返回的HTTP头部定向到indexFile文件对象
    c.setopt(pycurl.WRITEHEADER, indexFile)
    # 将返回的HTML内容定向到indexFile对象
    c.setopt(pycurl.WRITEDATA, indexFile)

    try:
        # 提交请求
        c.perform()
        # 获取DNS解析时间
        NAMELOOKUP_TIME = c.getinfo(pycurl.NAMELOOKUP_TIME) * 1000
        # 获取建立连接时间
        CONNECT_TIME = c.getinfo(pycurl.CONNECT_TIME) * 1000
        # 获取从建立连接到准备传输所消耗的时间
        PRETRANSFER_TIME = c.getinfo(pycurl.PRETRANSFER_TIME) * 1000
        # 获取从建立连接到传输开始消耗的时间
        STARTTRANSFER_TIME = c.getinfo(pycurl.STARTTRANSFER_TIME) * 1000
        # 获取传输的总时间
        TOTAL_TIME = c.getinfo(pycurl.TOTAL_TIME) * 1000
        # 获取HTTP状态码
        HTTP_CODE = c.getinfo(pycurl.HTTP_CODE)
        # 获取下载数据包大小
        SIZE_DOWNLOAD = c.getinfo(pycurl.SIZE_DOWNLOAD)
        # 获取HTTP头部大小
        HEADER_SIZE = c.getinfo(pycurl.HEADER_SIZE)
        # 获取平均下载速度
        SPEED_DOWNLOAD = c.getinfo(pycurl.SPEED_DOWNLOAD)

        # 关闭打开的文件
        indexFile.close()
        # 关闭Curl对象
        c.close()
        """
        # 打印看看
        print("%s %s \r\n"
              "HTTP状态码：%d \r\n"
              "DNS解析时间：%d ms\r\n"
              "建立连接时间：%d ms\r\n"
              "准备传输时间：%d ms\r\n"
              "传输开始时间：%d ms\r\n"
              "传输结束总时间：%d ms\r\n"
              "请求数据大小：%d betys\r\n"
              "HTTP头部大小：%d betys\r\n"
              "平均下载速度：%d betys/s\r\n" % (url_t[0],url,
                                                HTTP_CODE,
                                                NAMELOOKUP_TIME,
                                                CONNECT_TIME,
                                                PRETRANSFER_TIME,
                                                STARTTRANSFER_TIME,
                                                TOTAL_TIME,
                                                SIZE_DOWNLOAD,
                                                HEADER_SIZE,
                                                SPEED_DOWNLOAD))
        """
        # 返回检测结果元组给data
        return (HTTP_CODE,
                round(NAMELOOKUP_TIME),
                round(CONNECT_TIME),
                round(PRETRANSFER_TIME),
                round(STARTTRANSFER_TIME),
                round(TOTAL_TIME),
                round(SIZE_DOWNLOAD),
                round(HEADER_SIZE),
                round(SPEED_DOWNLOAD),
                time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                NODE,  # NODE引用自配置文件config
                url_t[0])

    # 检测出现异常时，做如下操作
    except Exception as e:
        # 先重新请求几次
        if check_number <= CHECK_NUM:
            # print(url_t[0], url, "第", check_number, "次检测出现异常：", e)
            check_number += 1
            return checkDomain(url_t, check_number)
        # 重试超过设定次数，则记录到数据库和文件，并且发送邮件
        else:
            # 获取数据库和游标
            conn, cursor = db_connect()
            # 引用event_type()获取事件类型id
            e = str(e)
            event_type_id = event_type(e)
            # 事件时间
            now_time = time.strftime("%Y-%m-%d  %H:%M:%S", time.localtime())
            # 获取url_id
            url_id = url_t[0]
            # print("\r\n节点", NODE, ",站点", url_id, url, ":连续", check_number - 1, "次检测均异常，保存异常结果到事件日志，并且发送邮件警告！\r\n")
            content = "%s  %s" % (url_t[1], e)
            try:
                # 分别捕获异常
                try: # 检测异常时，发送邮件
                    if (url_t[5] == 0) and (url_t[4] == 0) and (url_t[3] != 0) and (content is not None):
                        subprocess.getstatusoutput("echo '%s' | mail -s '站点异常:%s' 1574956497@qq.com" % (content, str(now_time)))
                        #subprocess.getstatusoutput("echo '%s' | mail -s '站点异常:%s' epay7777@gmail.com" % (content, str(now_time)))
                        print("\r\n节点", NODE, ",站点", url_id, url, ":连续", check_number - 1,"次检测均异常，发送邮件警告！\r\n")
                except Exception as e:
                    print("检测异常时，发送邮件失败：%s" % e)
                    # 记录异常日志
                    write_log(e)

                try: # 检测异常时，更新webmoni_domainname表中url的状态status_id
                    if event_type_id != url_t[3]:
                        cursor.execute(
                            'UPDATE webmoni_domainname SET status_id = %d where id = %d' % (event_type_id, url_id))
                        conn.commit()
                        print("\r\n节点", NODE, ",站点", url_id, url, ":连续", check_number - 1,"次检测均异常，更新域名状态！\r\n")
                    else:
                        print("\r\n节点", NODE, ",站点", url_id, url, ":连续", check_number - 1, "次检测均异常，更新域名状态！\r\n")
                except Exception as e:
                    print("检测异常时，更新webmoni_domainname表中url的状态status_id失败：%s" % e)
                    # 记录异常日志
                    write_log(e)

                try: # 检测异常时，保存异常事件信息到日志表webmoni_event_log
                    err_info = "'%d','%d','%d','%s'" % (event_type_id, NODE, url_id, now_time)
                    cursor.execute('insert into webmoni_event_log(event_type_id,node_id,url_id,datetime) value(%s)' % (err_info))
                    conn.commit()
                    print("\r\n节点", NODE, ",站点", url_id, url, ":连续", check_number - 1, "次检测均异常，记录事件日志！\r\n")
                except Exception as e:
                    print("检测异常时，保存异常事件信息到日志表webmoni_event_log失败：%s" % e)
                    # 记录异常日志
                    write_log(e)

                try:    # 检测异常时，继续保存空结果到表webmoni_monitordata
                    err_url = "'%s','%d','%d'" % (now_time, NODE, url_id)
                    cursor.execute('insert into webmoni_monitordata(datetime,node_id,url_id) value(%s)' % (err_url))
                    conn.commit()
                    print("\r\n节点", NODE, ",站点", url_id, url, ":连续", check_number - 1, "次检测均异常，记录空结果！\r\n")
                    # 检测异常时，返回False
                    return False
                except Exception as e:
                    print("检测异常时，继续保存空结果到表webmoni_monitordata失败：%s" % e)
                    # 记录异常日志
                    write_log(e)
                # 检测异常打印看看

            # 检测失败时，一定要返回False
            finally:
                # 关闭数据库连接
                db_close(cursor, conn)
                # 关闭打开的文件
                indexFile.close()
                # 关闭Curl对象
                c.close()
                return False


# 保存检测结果data到数据库
def resultSave(url_t,data):
    # 获取数据库和游标
    conn, cursor = db_connect()
    try:
        # 检测结果data插入到数据库
        cursor.execute("insert into webmoni_monitordata(http_code,"
                           "namelookup_time,"
                           "connect_time,"
                           "pretransfer_time,"
                           "starttransfer_time,"
                           "total_time,"
                           "size_download,"
                           "header_size,"
                           "speed_download,"
                           "datetime,"
                           "node_id,"
                           "url_id) value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", data)
        # 提交执行
        conn.commit()
        print("^保存成功:",data[-1],data,"\r\n")
        # 更新域名状态为正常
        if (url_t[3] != 0):
            cursor.execute('UPDATE webmoni_domainname SET status_id = %d where id = %d' % (0, url_t[0]))
            print('*'*20,'I am here')
            conn.commit()

    except Exception as e:
        print("保存检测结果时失败")
        # 记录保存结果出现异常的日志
        write_log(e)
        exit(e)

    finally:
        # 关闭数据库连接
        db_close(cursor,conn)


def main(url_t):
    check_number = 1
    data = checkDomain(url_t,check_number)
    if data != False:
        resultSave(url_t,data)

# 开始
if __name__ == '__main__':
    # 这里开始轮询
    while True:
        # 连接数据库
        conn, cursor = db_connect()
        # 查询出所有要检测的域名
        cursor.execute('select * from webmoni_domainname where (check_id = 0) ORDER BY id ASC')
        domains = cursor.fetchall()
        print(domains)
        # 关闭数据库连接
        db_close(cursor,conn)

        # 打印配置信息
        print("=" * 100, "\r\n设定轮询间隔时间：%ss" % INTERVAL)
        print("设定数据库操作失败时重试间隔时间：%ss" % RETRY)
        print("设定检测站点异常时重试次数：%s 次" % CHECK_NUM)
        print("设定请求超时时间：%ss" % TIME_OUT)
        print("设定线程/进程数：%s" % THREAD_NUM)
        print("设定检测节点ID： %s\r\n" % NODE, "-" * 98)
        print("此次轮询共有%s个域名待检测" % (len(domains)))

        # 设定轮询间隔时间
        time_remaining = INTERVAL - time.time() % INTERVAL
        now_time = (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        time2go = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time() + time_remaining))
        print("现在是：[%s]，[%s]开始执行，等待 %s second..." % (now_time, time2go, time_remaining))

        # 整点开始
        time.sleep(time_remaining)
        print("[", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "] It is Time to Go Go Go…\r\n","-"*98)
        star = time.time()

        # 创建进程池，进程数=THREAD_NUM，进程调用函数main，参数url_t
        try:
            pool = Pool(THREAD_NUM)
            for url_t in domains:
                pool.apply_async(func=main, args=(url_t,))
            # 终止创建子进程
            pool.close()
            # 等待所有子进程结束
            pool.join()
        except Exception as e:
            print(e)

        stop = time.time()
        print(stop-star)
