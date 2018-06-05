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



# 前端输入登录名和密码，传输md5加密密码
def inputLogin():
    #接收用户的输入
    loginname = input("请输入登录名:")
    loginpawd = input("请输入密码:")

    MD5 = hashlib.md5()
    MD5.update(loginpawd.encode(encoding='utf-8'))
    md5loginpawd = MD5.hexdigest()
    return loginname,md5loginpawd


# 后端接收登录名和MD5加密密码，再次加密后保存到数据库
def addLogin():
    # 接收第一次加密的密码
    loginname,loginpawd = inputLogin()
    print(loginname,loginpawd)
    # 进行第二次加密
    MD5 = hashlib.md5()
    MD5.update(loginpawd.encode(encoding='utf-8'))
    md5loginpawd = MD5.hexdigest()
    # 存储第二次加密的密码
    user_info = "'%s','%s'"%(loginname,md5loginpawd)
    conn, cursor = db_connect()
    try:
        cursor.execute('insert into user_login(user_name,user_pw) value(%s)' % user_info)
        conn.commit()
    except pymysql.err.IntegrityError as e:
        print(e)
    finally:
        db_close(cursor,conn)

# 创建用户
#addLogin()

# 登录
def login(users_list,user_name_list):

    i=1
    while i<=3:
        # 用户输入登录名和密码
        loginname, loginpawd = inputLogin()
        # 进行第二次加密
        MD5 = hashlib.md5()
        MD5.update(loginpawd.encode(encoding='utf-8'))
        md5loginpawd = MD5.hexdigest()
        # 验证再次加密的密码

        if loginname not in user_name_list:
            print("用户不存在,剩余次数%d"% int(3 - i))
            i+=1
        elif (loginname in user_name_list) and ([loginname, md5loginpawd] not in users_list):
            print("密码输入错误,剩余次数%d"% int(3 - i))
            i+=1
        elif([loginname, md5loginpawd] in users_list):
            print('登录成功')
            break
        else:
            print("输入有误，重新输入，剩余次数%d"% int(3 - i))
            i+=1
    else:
        print("错的太多，不能登录，IP拉黑")


if __name__ == '__main__':
    # 用户验证密码库
    conn, cursor = db_connect()
    try:
        cursor.execute('SELECT * FROM user_login WHERE no_login = 1')
        user_list = []
        user_name_list = []
        # 拿到用户名密码列表user_list
        for user_infos in cursor.fetchall():
            user_info = []
            user_info.append(user_infos[1])
            user_info.append(user_infos[2])
            user_list.append(user_info)
        # 拿到登录用户列表user_name_list
        for user_name in user_list:
            user_name_list.append(user_name[0])

        login(user_list,user_name_list)



    except Exception as e:
        print(e)
    finally:
        db_close(cursor,conn)

