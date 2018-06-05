import socket, sys
from OpenSSL import SSL

ctx = SSL.Context(SSL.SSLv23_METHOD)

print("Creating socket")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print()
ssl = SSL.Connection(ctx, s)

print("Establishing Connection")
ssl.connect(("www.baidu.com", 443))
print("done")

print("Requesting Documents")
print("done")

try:
    buf = ssl.read(4096)
    print(str(buf))
    sys.stdout.write(buf)
except SSL.ZeroReturnError:
    print("1")


ssl.send("USER username")

try:
    buf2 = ssl.recv(4096)
    sys.stdout.write(buf2)
except SSL.ZeroReturnError:
    print("2")


ssl.send("PASS secret")

try:
    buf3 = ssl.read(4096)
    sys.stdout.write(buf3)
except SSL.ZeroReturnError:
    print("2")


print("connected")
ssl.close()
