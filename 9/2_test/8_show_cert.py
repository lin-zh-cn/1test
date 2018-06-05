import time
import datetime

cert = {'subject': ((('commonName', 'tm33.net'),),), 'issuer': ((('countryName', 'US'),), (('organizationName', "Let's Encrypt"),), (('commonName', "Let's Encrypt Authority X3"),)), 'version': 3, 'serialNumber': '0335DA1BC3E454C13E4B6BD3518CBA9CCA4A', 'notBefore': 'Apr 19 05:54:09 2018 GMT', 'notAfter': 'Jul 18 05:54:09 2018 GMT', 'subjectAltName': (('DNS', 'tm33.net'),), 'OCSP': ('http://ocsp.int-x3.letsencrypt.org',), 'caIssuers': ('http://cert.int-x3.letsencrypt.org/',)}
for items in cert.items():
    print(items)


# 有效期开始
notBefore = cert['notBefore']
notBefore = time.mktime(time.strptime(notBefore,'%b %d %H:%M:%S %Y %Z'))
# 有效期结束
notAfter = cert['notAfter']
notAfter = time.mktime(time.strptime(notAfter,'%b %d %H:%M:%S %Y %Z'))
# 当前时间
nowDate = time.time()
# 时间差
expire = (notAfter - nowDate)/3600/24
# 时间格式本地化
startDate = time.strftime("%Y-%m-%d",time.localtime(notBefore))
endDate = time.strftime("%Y-%m-%d",time.localtime(notAfter))
print("证书有效期%s至%s,"%(startDate,endDate),"还有%s天到期"%int(expire))

