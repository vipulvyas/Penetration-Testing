# Troubleshooting 
## Gathering informtion :: [Hardware](#hardware) | [Network](#network) | [Registry](#registry) | [File and Printers](#file-and-printer) | [Active Directory](#active-directory)

### overview
- Get-Command
  - Help
    - Get-member 
#### Windows Management Instrumentation (WMI) (powershell 3 or lower) which use for information of operating system which is base on Common Information Model (CIM) 
```
Get-WMIobject 
Get-CimInstance
```

## Hardware

#### memory counter
```
get-command *counter*
Get-Counter # allow all memory, Porcessor, phisical Disk
get-counter -listset *memory*  # list all memory counter
get-counter -listset *memory* | where countersetname -eq 'memory' | select -expand paths  # expand is user for display all path in given countersetname (... display all)
get-counter "select path from above list" # show count
get-ciminstance win32_physicalmemory   # get data from win32 classes and dispaly all the physical memory information
```
#### Disk information
```
get-cimclass -classname *disk* 
get-wmiobject -Class Win32_logicalDisk
```
#### BIOS information
```
get-cimclass *BIOS* # win32_BIOS is a bios related class
get-WMIobject Win32_BIOS
get-ciminstance win32_BIOS
```
#### display when system rebooted last
```
gcm *event*
help get-eventlog
help get-eventlog -example
get-eventlog -log system -newest 1000 | where-object eventid -eq '1074' | format-table machinename, username, timegenerated -autosize
```

## Network
#### ip configuration
```
ipconfig /all
gcm *ip*
get-netipaddress
get-netipconfiguration
```
#### DNS
```
gcm *DNS*
help get-DNSclient
get-dnsclent
get-dnsclentserver
get-dnsclientchache
```

#### SMB

```
gcm *SMB*
help get-smbmapping -example
get-smbmapping # display all mapping
help new-smbmapping -example
New-smbmapping -LocalPath S: -RemotePath \\DCO1\Shares
get-smbmapping
```

#### ping and tracert
```
ping ip
tracert ip
Test-Netconnection ip # same as ping
Test-Netconnection ip -TraceRoute  # same as tracert
Test-Netconnection -CommonTCPPort [HTTP | RDP | SMB | WINRM] -ComputerName google.com  # it use ping and tcp both
```
## Registry

#### change in registry it direct impact to system so take backup
#### if packegeinstalled is 1 than it is installed on machine if you want to reinstall it than set it to 0 so whenever user login than it reinstall 

```
help get-psprovider # powershell provider
get-psprovider
set-location HKLM:   # Registry user so set to that location HKML:\software
set-ItemProperty -path .\wirebratinCoffee(path of applicatoin) -name PackageInstalled -value 0
```
## File And Printer
#### list file
```
help get-childItem -example
get-childitem -path M:\ -Recurse -Include *.PNG  # all png file in M:\
```
#### copy file
```
gcm *copy*
help copy-item -example
copy M:\DdesktopBackgrounds -Destination C:\Backgrounds -Recurse -Verbose
```
#### move file or folder
```
move-item C:\Backgrounds -Detination C:\MovedFolder -verbose
```
 
#### Rename folder or file
```
rename-item c:\movedfolder -newname c:\RenamedFolder
```

#### file permission
```
icacls.exe | more  # display how to use view,set permission
icacls M:\desktopfolder
```

#### printer
```
gcm *printer*
get-printer # all printer
get-printer -Computername DCO1
help add-printer
add-printer -connectionname \\dco1\MKTG-PR-101
get-printer
remover-printer -name "printer name from above list"
```

## Active Directory
#### user Detail
```
gcm *user*
help get-aduser
help get-aduser -example
get-aduser -Identity "username" -properties * | more
```
#### get locked or Disable Account
```
search-adAccount -lockedout | select name # display all AD locked Account
search-adAccount -AccountDiable | select name  #display disable account
```
#### AD Compuer Detail
```
get-adcomputer -Filter *   # display all computer name
get-adcomputer -Identity [CLient02 | computername] -Properties * | more  # get detail about compuer like os ,accounts
```
#### group info
```
get-command *group*
help get-adgroup -example
get-adgroup -filter *
get-adgroup -filter * | where name -like "*MKTG*"  # group name like marketing share group
get-adgroup -filter {name -like "*MKTG*" } # same as above
```
#### add group member
```
get-admember -Identity "MKTG User" | select name
add-adgroupmember     # add member in group
```
#### get which member is in MKTG and in city seattle
```
get-aduser -filter * -properties * | get-member | more
get-aduser -Property name,city,department -filter {Department -eq "MKTG" -and city -eq "seattle"} | FT samaccountname,city,Department -autosize > seattle.txt    # it give table format 
```

