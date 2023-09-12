IP = 10.10.10.59

Nmap (nmap -p- -Pn 10.10.10.59)
```bash
PORT     STATE SERVICE      REASON
21/tcp   open  ftp          syn-ack
80/tcp   open  http         syn-ack
81/tcp   open  hosts2-ns    syn-ack
135/tcp  open  msrpc        syn-ack
139/tcp  open  netbios-ssn  syn-ack
445/tcp  open  microsoft-ds syn-ack
808/tcp  open  ccproxy-http syn-ack
1433/tcp open  ms-sql-s     syn-ack
```

Nmap ()
```bash
RT     STATE SERVICE       VERSION
21/tcp   open  ftp           Microsoft ftpd
| ftp-syst:
|_  SYST: Windows_NT
80/tcp   open  http          Microsoft IIS httpd 10.0
|_http-generator: Microsoft SharePoint
| http-title: Home
|_Requested resource was http://10.10.10.59/_layouts/15/start.aspx#/default.aspx
|_http-server-header: Microsoft-IIS/10.0
81/tcp   open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Bad Request
|_http-server-header: Microsoft-HTTPAPI/2.0
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds  Microsoft Windows Server 2008 R2 - 2012 microsoft-ds
808/tcp  open  ccproxy-http?
1433/tcp open  ms-sql-s      Microsoft SQL Server 2016 13.00.1601.00; RTM
| ms-sql-ntlm-info:
|   Target_Name: TALLY
|   NetBIOS_Domain_Name: TALLY
|   NetBIOS_Computer_Name: TALLY
|   DNS_Domain_Name: TALLY
|   DNS_Computer_Name: TALLY
|_  Product_Version: 10.0.14393
| ssl-cert: Subject: commonName=SSL_Self_Signed_Fallback
| Not valid before: 2022-02-19T11:25:06
|_Not valid after:  2052-02-19T11:25:06
|_ssl-date: 2022-02-19T11:45:28+00:00; -3s from scanner time.
Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode:
|   3.1.1:
|_    Message signing enabled but not required
|_clock-skew: mean: -3s, deviation: 0s, median: -4s
| smb-security-mode:
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-time:
|   date: 2022-02-19T11:45:20
|_  start_date: 2022-02-19T11:24:46
| ms-sql-info:
|   10.10.10.59:1433:
|     Version:
|       name: Microsoft SQL Server 2016 RTM
|       number: 13.00.1601.00
|       Product: Microsoft SQL Server 2016
|       Service pack level: RTM
|       Post-SP patches applied: false
|_    TCP port: 1433

```

Login page (http://10.10.10.59/_layouts/15/Authenticate.aspx?Source=%2F%5Flayouts%2F15%2Fstart%2Easpx)
```bash
CREDENTIALS:

```

Login page2 (http://10.10.10.59/_vti_bin/owssvr.dll)
```
CREDENTIALS:
```

Login page3 (http://10.10.10.59/_layouts/wrkmng.aspx)
```
CREDENTIALS:
```

Listing of other paths (http://10.10.10.59/_vti_bin/spdisco.aspx)

ffuf (ffuf -u http://10.10.10.59/FUZZ -w sharepoint.txt --fw 6)
```bash
_vti_bin/dws.asmx       [Status: 200, Size: 4827, Words: 1598, Lines: 149]                             [4/274]
_vti_bin/Authentication.asmx [Status: 200, Size: 3264, Words: 671, Lines: 86]                                 
_vti_inf.html           [Status: 200, Size: 247, Words: 5, Lines: 8]                                          
_vti_bin/diagnostics.asmx [Status: 200, Size: 3227, Words: 588, Lines: 81]                                    
_vti_bin/copy.asmx      [Status: 200, Size: 3418, Words: 774, Lines: 93]                                      
_vti_bin/imaging.asmx   [Status: 200, Size: 4877, Words: 1598, Lines: 149]
_vti_bin/People.asmx    [Status: 200, Size: 3446, Words: 774, Lines: 93]
_vti_bin/permissions.asmx [Status: 200, Size: 4114, Words: 1083, Lines: 114]
_vti_bin/forms.asmx     [Status: 200, Size: 3240, Words: 671, Lines: 86]
_vti_bin/meetings.asmx  [Status: 200, Size: 5204, Words: 1701, Lines: 156]
_vti_bin/lists.asmx     [Status: 200, Size: 9066, Words: 3761, Lines: 296]
_vti_bin/WebPartPages.asmx [Status: 200, Size: 8696, Words: 3349, Lines: 268]
_vti_bin/views.asmx     [Status: 200, Size: 4316, Words: 1289, Lines: 128]
_vti_bin/webs.asmx      [Status: 200, Size: 6886, Words: 2628, Lines: 219]
_vti_bin/UserGroup.asmx [Status: 200, Size: 11708, Words: 4997, Lines: 380]
_vti_bin/spsearch.asmx  [Status: 200, Size: 3714, Words: 902, Lines: 102]
_vti_bin/sites.asmx     [Status: 200, Size: 4927, Words: 1598, Lines: 149]
_vti_bin/spdisco.aspx   [Status: 200, Size: 6160, Words: 256, Lines: 47]
_vti_bin/alerts.asmx?wsdl [Status: 200, Size: 8386, Words: 1411, Lines: 174]
_vti_bin/SiteData.asmx  [Status: 200, Size: 5448, Words: 1907, Lines: 170]
_layouts/MyInfo.aspx    [Status: 200, Size: 8717, Words: 290, Lines: 161]
_Layouts/RedirectPage.aspx [Status: 200, Size: 8723, Words: 290, Lines: 161]
_layouts/AreaTemplateSettings.aspx [Status: 200, Size: 8731, Words: 290, Lines: 161]
_layouts/Policylist.aspx [Status: 200, Size: 8721, Words: 290, Lines: 161]
_layouts/sitemanager.aspx [Status: 200, Size: 8722, Words: 290, Lines: 161]
_layouts/PageSettings.aspx [Status: 200, Size: 8723, Words: 290, Lines: 161]
_layouts/policy.aspx    [Status: 200, Size: 8717, Words: 290, Lines: 161]
_layouts/policycts.aspx [Status: 200, Size: 8720, Words: 290, Lines: 161]
_layouts/policyconfig.aspx [Status: 200, Size: 8723, Words: 290, Lines: 161]
_layouts/wrkmng.aspx    [Status: 401, Size: 16, Words: 2, Lines: 1]
```

Version disclosure (http://10.10.10.59/_vti_inf.html)
```
<!-- FrontPage Configuration Information 
FPVersion="15.00.0.000"
FPShtmlScriptUrl="_vti_bin/shtml.dll/_vti_rpc"
FPAuthorScriptUrl="_vti_bin/_vti_aut/author.dll"
FPAdminScriptUrl="_vti_bin/_vti_adm/admin.dll"
TPScriptUrl="_vti_bin/owssvr.dll"
-->
```

Nikto scan
```bash
+ Server: Microsoft-IIS/10.0
+ Retrieved microsoftsharepointteamservices header: 15.0.0.4420
+ Retrieved x-powered-by header: ASP.NET
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ Uncommon header 'request-id' found, with contents: 5b4122a0-2cd1-f075-0000-0fa86536e5f0
+ Uncommon header 'sprequestduration' found, with contents: 2381
+ Uncommon header 'x-ms-invokeapp' found, with contents: 1; RequireReadOnly
+ Uncommon header 'microsoftsharepointteamservices' found, with contents: 15.0.0.4420
+ Uncommon header 'spiislatency' found, with contents: 122
+ Uncommon header 'sprequestguid' found, with contents: 5b4122a0-2cd1-f075-0000-0fa86536e5f0
+ Uncommon header 'x-sharepointhealthscore' found, with contents: 5
+ Root page / redirects to: http://10.10.10.59/_layouts/15/start.aspx#/default.aspx
+ Uncommon header 'public-extension' found, with contents: http://schemas.microsoft.com/repl-2
+ Retrieved x-aspnet-version header: 4.0.30319
+ Uncommon header 'sharepointerror' found, with contents: 0
+ OSVDB-68127: Server may be vulnerable to https://docs.microsoft.com/en-us/security-updates/securitybulletins/2010/MS10-070 (based on numeric calculation), thus allowing a cryptographic padding oracle. This vulnerabilty must be manually validated. See http://blog.gdssecurity.com/labs/2010/9/14/automated-padding-oracle-attacks-with-padbuster.html

```

ffuf (ffuf -u http://10.10.10.59/FUZZ -w ./Discovery/Web-Content/CMS/sharepoint.txt --fw 6,290)
```bash
_layouts/1033/avreport.htm [Status: 200, Size: 7478, Words: 1316, Lines: 139]
_layouts/1033/fontdlg.htm [Status: 200, Size: 3123, Words: 259, Lines: 110]
_layouts/1033/error.htm [Status: 200, Size: 5497, Words: 730, Lines: 139]
_layouts/1033/filedlg.htm [Status: 200, Size: 5767, Words: 1673, Lines: 127]
_layouts/1033/iframe.htm [Status: 200, Size: 430, Words: 26, Lines: 14]
_layouts/1033/instable.htm [Status: 200, Size: 4169, Words: 209, Lines: 147]
_layouts/1033/menubar.htc [Status: 200, Size: 13957, Words: 4875, Lines: 390]
_layouts/1033/menu.htc  [Status: 200, Size: 21817, Words: 1508, Lines: 749]
_layouts/1033/selcolor.htm [Status: 200, Size: 12165, Words: 4610, Lines: 258]
_layouts/1033/spthemes.xml [Status: 200, Size: 5541, Words: 397, Lines: 132]
_layouts/1033/spthemes.xsd [Status: 200, Size: 1150, Words: 40, Lines: 25]
_catalogs/masterpage/forms/allitems.aspx [Status: 200, Size: 64514, Words: 3915, Lines: 593]
_catalogs/wp/forms/allitems.aspx [Status: 200, Size: 63493, Words: 3854, Lines: 586]
_catalogs/lt/forms/allitems.aspx [Status: 200, Size: 54500, Words: 3571, Lines: 586]
_layouts/images/        [Status: 403, Size: 0, Words: 1, Lines: 1]
_layouts/pickerresult.aspx [Status: 200, Size: 935, Words: 33, Lines: 25]
_layouts/sendtoofficialfile.aspx [Status: 401, Size: 16, Words: 2, Lines: 1]
_vti_inf.html           [Status: 200, Size: 247, Words: 5, Lines: 8]
default.aspx            [Status: 200, Size: 38709, Words: 1, Lines: 1]
shared documents/forms/allitems.aspx [Status: 200, Size: 60293, Words: 4884, Lines: 761]

```

Ftp creds:
```
CREDENTIALS:
password: UTDRSCH53c"$6hys
```

Keepass creds:
```
CREDENTIALS:
tim : simplementeyo
```