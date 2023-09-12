#!/usr/bin/env python3

import requests

url = "http://127.0.0.1:"
proxy = {"http":"http://kalamari:ihateseafood@joker:3128/"}

for i in range(0,65536):
    req = requests.get(url+str(i),proxies=proxy)
    if req.status_code != 503 and req.status_code != 403:
        print("We got a hit on port %s!" %str(i))
