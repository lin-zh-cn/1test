from PIL import Image,ImageDraw,ImageFont,ImageFilter
from io import BytesIO,StringIO
import random
import string
import secrets
import hashlib
from django.shortcuts import render,redirect
from login.models import *
from django.shortcuts import HttpResponse

# 登录
def login(request):
    if request.method == "GET":
        err = {"loginerr":"请先登录"}
        return render(request,'login.html', err)

    if request.method == "POST":
        # 获取用户输入
        loginname = request.POST.get('user')
        loginpw = request.POST.get('password')
        verifycode = request.POST.get('verifycode')

        # 获取验证码字符
        verifyCodeText = request.session.get('verifyCodeText')

        # 密码MD5加密处理
        MD5 = hashlib.md5()
        MD5.update(loginpw.encode(encoding='utf-8'))
        md5_loginpw = MD5.hexdigest()

        # 验证码校验
        if verifyCodeText == verifycode :
            # 获取用户列表
            user_list = []
            for user_info in User.objects.filter(no_login=1):
                user_list.append(user_info.user_name)
            # 验证用户名是否存在
            if loginname in user_list:
                # 获取数据库中用户对应的加盐加密密码
                user_pw = (User.objects.get(user_name=loginname)).user_pw
                # 去盐，得到加密过的密码
                user_md5pw = user_pw[54:67]+user_pw[24:43]
                # 验证码校验
                if md5_loginpw == user_md5pw and verifycode == verifyCodeText:
                    # 保存session，关闭浏览器就过期
                    request.session['user'] = loginname
                    request.session['password'] = loginpw
                    request.session.set_expiry(0)
                    return redirect('/index/')
                else:
                    err = {"loginerr": "密码错误"}
                    return render(request, 'login.html', err)
            else:
                err = {"loginerr": "用户不存在"}
                return render(request, 'login.html', err)
        else:
            err = {"loginerr": "验证码错误"}
            return render(request, 'login.html', err)

# 登出
def logout(request):
    # 删除失效的session
    request.session.clear_expired()
    # 清空session
    request.session.clear()
    # 转到登录页
    return render(request, 'login.html')

# 创建登录用户
def add_login():
    # 获取用户列表
    user_list = []
    for user_info in User.objects.all():
        user_list.append(user_info.user_name)
    print(user_list)
    # 获取用户输入
    while True:
        loginname = input("请输入登录名:")
        loginpw = input("请输入密码:")
        if loginname not in user_list and len(loginname) > 3 and len(loginpw) > 8:
            break
        elif loginname in user_list:
            print("用户已存在")
        else:
            print("输入有误，用户名至少4位，密码至少9位")
    print(loginname, loginpw)
    # MD5加密
    MD5 = hashlib.md5()
    MD5.update(loginpw.encode(encoding='utf-8'))
    hashpw = MD5.hexdigest()
    print("登录名是：", loginname, "加密密码：", hashpw,len(hashpw))
    print(hashpw)
    # 构造加盐密码
    pw = []
    with open('login/words') as f:
        words = [word.strip() for word in f]
    for i in range(3):
        pw1 = secrets.choice(words)
        pw.append(pw1)
    pw2 = "".join(secrets.choice(string.ascii_letters + string.digits) for i in range(11))
    pw3 = "".join(secrets.choice(string.ascii_letters + string.digits) for i in range(61))
    pw.append(hashpw[13:])
    pw.append(pw2)
    pw.append(hashpw[:13])
    pw.append(pw3)
    password = ''.join(pw)
    print("登录名是：",loginname,"密码加盐：",password,len(password))
    # 存储加密加盐的密码
    try:
        User.objects.create(user_name=loginname, user_pw=password)
    except Exception as e:
        print(e)

#add_login()

# 验证码
def verifyCode(request):
    # 背景色，宽高
    bgColor = (random.randrange(20,100),random.randrange(20,100),255)
    width = 160
    height = 36

    # 创建画布对象
    im = Image.new('RGB',(width,height))

    # 创建画笔对象
    draw = ImageDraw.Draw(im)

    # 调用画笔的point()绘制噪点,搞点彩线嘿嘿嘿
    for x in range(width):
        fillColor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        for y in range(height):
            draw.point((x, y), fill=(fillColor))

    # 定义验证码字符选择范围
    textChoice = "acdefghkmnpstwxy23456789"
    # 定义验证码字体和大小
    font = ImageFont.truetype('C:\Windows\Fonts\Arial.TTF', 28)
    # 随机4个字符写入画布
    verifyCodeText = ""
    for t in range(4):
        textRnd = random.choice(textChoice)
        verifyCodeText+=textRnd
        draw.text((40 * t + 10, 1),textRnd, font=font)
    # 验证码文本
    request.session.clear()
    request.session['verifyCodeText'] = verifyCodeText
    request.session.set_expiry(600)
    # 删除画笔
    del draw
    # 模糊处理，模糊半径参数可调
    verifyCode = im.filter(ImageFilter.BoxBlur(1.1))

    # 验证码图片流保存到内存
    buf2 = BytesIO()
    verifyCode.save(buf2, "png")

    return HttpResponse(buf2.getvalue(),'image/png')
