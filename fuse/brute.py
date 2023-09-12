#!/usr/bin/env python3

import requests

url = "http://fuse.fabricorp.local/papercut/logs/html/papercut-print-log-2020-"

for m in range(1,13):
    if m < 10:
        month = "0" + str(m)
    else:
        month = str(m)
    for d in range(1,32):
        if d < 10:
            day = "0" + str(d)
        else:
            day = str(d)
        prefix = month + "-" + day + ".htm"
        req = requests.get(url + prefix)
        if req.status_code != 404:
            print("We got a hit!: %s" %url+prefix)
