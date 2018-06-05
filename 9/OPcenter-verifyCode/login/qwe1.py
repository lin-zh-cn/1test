from PIL import Image,ImageDraw,ImageFont,ImageFilter
from io import BytesIO,StringIO
import random
import string
import secrets
import hashlib
from django.shortcuts import render,redirect

from django.shortcuts import HttpResponse


loginuser = 'root@qq.com'
loginpw = 'Kemingjunde!@#'

strs = loginuser + '@' + loginpw


MD5 = hashlib.md5()
MD5.update(strs.encode(encoding='utf-8'))
md5_loginpw = MD5.hexdigest()

print(md5_loginpw)
