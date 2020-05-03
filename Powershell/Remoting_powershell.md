# Remoting
## Based on [Winrm](https://docs.microsoft.com/en-us/windows/win32/winrm/portal)
## must Enable PS_remoting
## set PSSESSION permission
## set Windows firewall for run set- command 


#### enable remoting required ADMIN
```
Enable-PSRemoting
```
#### PSSESSION permission required ADMIN
```
set-PSSessionConfiguration -Name Microsoft.Powershell -ShowSecurityDescriporUI
```
#### Enter in computer session
```
Enter-PSSession -ComputerName Client02
```
#### Display trusted hosts
```
get-item WSMAN:\localhost\Client\TrustedHosts
```
#### set trusted hosts
```
set-item WSMAN:\localhost\Client\TrustedHosts -Value [* | Computername]
```
#### get firewall rule
```
get-NetFirewallrule | where DisplayName -Like "*windows management Tnstumentation*" | select Displayname, name, enable
```
#### set firewall rule
```
get-NetFirewallrule | where DisplayName -Like "*windows management Tnstumentation*" | set-NetFirewallrule -Enable True -Verbose
```
#### PSSEssion
```
gcm *-PSSession*
Enter-PSSESSIon -Computername $computername
get-service -Comp $computername | select name ,status
EXIT  # exit from that session
get-PSSESSIO | Remove-PSSESSIOn
```
#### Invoke command run script remotely or run a block
```
help invoke-command -example
invoke-command -computername $computername -ScriptBlock {get-service | select name,status} | out-file service.txt #run block
```

#### cimsession same as pSSession use when module or set of cmdlet like dnsclient
```
get-DNSClientServerAddress -CimSession (New-CimSession -compuername $computername) # '()' use for nested command and this command giving DNS information
```




