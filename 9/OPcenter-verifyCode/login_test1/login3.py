import secrets
import string
import hashlib
import pymysql
from config import *

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
        print("建立数据库连接出现异常",e)

# 关闭数据库连接
def db_close(cursor,conn):
    try:
        # 关闭游标
        cursor.close()
        # 关闭连接
        conn.close()
    except Exception as e:
        print("关闭数据库连接出现异常",e)

# 前端输入登录名和密码
def input_login():
    while True:
    #接收用户的输入
        loginname = input("请输入登录名:")
        loginpw= input("请输入密码:")
        if len(loginname) > 3 and len(loginpw) > 8:
            break
        else:
            print("输入有误，用户名至少4位，密码至少9位")
    return loginname, loginpw

# 后端接收登录名和MD5加密密码，再次加密后保存到数据库
def add_login():
    # 获取用户名密码库
    user_list, user_name_list = get_login_list()
    # 获取用户输入
    loginname, loginpw = input_login()
    if loginname in user_name_list:
        print("添加失败，用户名已存在")
        exit()

    # MD5加密
    MD5 = hashlib.md5()
    MD5.update(loginpw.encode(encoding='utf-8'))
    hashpw = MD5.hexdigest()
    print("登录名是：", loginname, "加密密码：", hashpw,len(hashpw))
    print(hashpw)
    # 构造加盐密码
    pw = []
    with open('./words') as f:
        words = [word.strip() for word in f]
    for i in range(3):
        pw1 = secrets.choice(words)
        pw.append(pw1)
    pw2 = "".join(secrets.choice(string.ascii_letters + string.digits) for i in range(11))
    pw3 = "".join(secrets.choice(string.ascii_letters + string.digits) for i in range(61))
    pw.append(hashpw[:13])
    pw.append(pw2)
    pw.append(hashpw[13:])
    pw.append(pw3)
    password = ''.join(pw)
    print("登录名是：",loginname,"密码加盐：",password,len(password))
    # 存储加密加盐的密码
    user_info = "'%s','%s'"%(loginname,password)
    conn, cursor = db_connect()
    try:
        cursor.execute('insert into user_login(user_name,user_pw) value(%s)' % user_info)
        conn.commit()
    except pymysql.err.IntegrityError as e:
        print(e)
    finally:
        db_close(cursor,conn)

# 获取用户名密码库
def get_login_list():
    # 连接数据库获取用户名和密码
    conn, cursor = db_connect()
    try:
        cursor.execute('SELECT * FROM user_login WHERE no_login = 1')
        # 用户名和密码列表
        user_db_list = []
        # 用户名列表
        user_name_list = []
        # 拿到用户名密码列表user_list
        for user_infos in cursor.fetchall():
            user_info = []
            user_info.append(user_infos[1])
            user_info.append(user_infos[2])
            user_db_list.append(user_info)
        # 密码去盐
        user_md5pw_list = []
        for user_pw in user_db_list:
            user_md5pw = [user_pw[0], (user_pw[1][24:37] + user_pw[1][48:67])]
            user_md5pw_list.append(user_md5pw)

        # 拿到登录用户列表user_name_list
        for user_name in user_db_list:
            user_name_list.append(user_name[0])
        return user_md5pw_list,user_name_list
    except Exception as e:
        print(e)
    finally:
        db_close(cursor, conn)

# 登录密码认证
def login():
    # 获取用户名密码列表
    user_md5pw_list, user_name_list = get_login_list()
    # 获取前端用户输入的用户名密码
    i = 1
    while i <= 3:
        # 用户输入登录名和密码
        loginname, loginpawd = input_login()
        # 密码进行md5加密
        MD5 = hashlib.md5()
        MD5.update(loginpawd.encode(encoding='utf-8'))
        md5loginpawd = MD5.hexdigest()

        # 验证密码
        if loginname not in user_name_list:
            print("用户不存在,剩余次数%d" % int(3 - i))
            i += 1
        elif (loginname in user_name_list) and ([loginname, md5loginpawd] not in user_md5pw_list):
            print("密码输入错误,剩余次数%d" % int(3 - i))
            i += 1
        elif ([loginname, md5loginpawd] in user_md5pw_list):
            print('登录成功')
            break
        else:
            print("输入有误，重新输入，剩余次数%d" % int(3 - i))
            i += 1
    else:
        print("错的太多，不能登录，IP拉黑")

login()

#add_login()

