,============== Enumeration ==============
IP: 10.10.10.73

Nmap (nmap -sC -sV -Pn 10.10.10.73)
```bash
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 36:c0:0a:26:43:f8:ce:a8:2c:0d:19:21:10:a6:a8:e7 (RSA)
|   256 cb:20:fd:ff:a8:80:f2:a2:4b:2b:bb:e1:76:98:d0:fb (ECDSA)
|_  256 c4:79:2b:b6:a9:b7:17:4c:07:40:f3:e5:7c:1a:e9:dd (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
| http-robots.txt: 1 disallowed entry 
|_/*.txt
|_http-title: Falafel Lovers
|_http-server-header: Apache/2.4.18 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

Nmp (nmap -p- 10.10.10.73)
```bash
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http
```

ffuf (ffuf -u 'http://falafel.htb/FUZZ' -w raft-large-words.txt -e .php --fc 403)
```bash
images                  [Status: 301, Size: 311, Words: 20, Lines: 10]
index.php               [Status: 200, Size: 7203, Words: 774, Lines: 110]
js                      [Status: 301, Size: 307, Words: 20, Lines: 10]
login.php               [Status: 200, Size: 7063, Words: 878, Lines: 103]
css                     [Status: 301, Size: 308, Words: 20, Lines: 10]
logout.php              [Status: 302, Size: 0, Words: 1, Lines: 1]
profile.php             [Status: 302, Size: 9787, Words: 1292, Lines: 259]
uploads                 [Status: 301, Size: 312, Words: 20, Lines: 10]
upload.php              [Status: 302, Size: 0, Words: 1, Lines: 1]
assets                  [Status: 301, Size: 311, Words: 20, Lines: 10]
style.php               [Status: 200, Size: 6174, Words: 690, Lines: 69]
footer.php              [Status: 200, Size: 0, Words: 1, Lines: 1]
header.php              [Status: 200, Size: 288, Words: 10, Lines: 18]
.                       [Status: 200, Size: 7203, Words: 774, Lines: 110]
connection.php          [Status: 200, Size: 0, Words: 1, Lines: 1]
authorized.php          [Status: 302, Size: 0, Words: 1, Lines: 1]

```
# ffuf with dir-medium gives same result

ffuf (ffuf -u http://10.10.10.73 -w raft-large-words.txt -H 'Host: FUZZ.falafel.htb' --fw 774)
```bash
NO VHOST FOUND
```


============== Enumeration End ==============

Creds: 240610708
admin 0e462096931906507119562988736854 
chris d4ee02a22fc872e36d9e3751ba72ddc8 (juggling)

USER:
moshe : falafelIsReallyTasty
yossi : MoshePlzStopHackingMe!

/usr/lib/git-core/git-credential-cache
/var/mail
/run/user/1001/systemd
/etc/crontab
/usr/share/gcc-5

/dev/snd/seq                                                                                                 
/dev/snd/timer                                                                                               
/dev/fb0                                                                                                     
/dev/dri/card0                                                                                               
/dev/dri/renderD128                                                                                          
/dev/dri/controlD64