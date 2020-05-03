## [Basic Command](#commands) | [help function](#help-function) | [Updating help](#update-help) | [Researching tool](#researching-tool) | [Get History](#history) | [PipeLining](#pipelining) | [Formatting](#formatting)
## Commands
#### write on powershell like echo
```
write-output "hello $home"  # hello home/hasky
write-output 'hello $home'  # hello $home
```
#### all verbs (For Data ,Life cycle , Diagnostic, Communication , Security etc)
```
get-verb | more
```

#### regex for verb
```
get-verb -verb S*
```
#### gscis for aliace for get-service
```
gsv
```

#### get Service name start with M in Computer Client1 and DCO1
```
get-service -Name M* -ComputerName Client1,DCO1
```
#### or powershell autometically detect first argument is -Name
```
gsv M* -ComputerName Client1,DCO1
```
#### or use short form and that should not conflict
```
gsv M* -comp Client1,DCO1
```

## help function
```
get-help
```

#### find DNS commands
```
get-help *DNS* |more
```

### Cmdlet is bult in tool in .NET , no argument :: Function take argument, function is created using comlet and other code

#### get-help module
```
get-help get-service |more
```
#### help = get-help <command> |more
#### above give info how to use like bellow
```
help get-service -example
```

#### all about file and it help for diffrent key terms and how to use it
```
help *about*
help about_aliases
```

## update help
```
update-help
```
## researching tool

#### get help for get-command
```
help get-command
help get-command -example
```
#### command type cmdlet and regex
```
get-command -type cmdlet
get-cimmand -verb New*
```

#### work with IP configuration for own computer
```
get-command -name *IP*
get-command -name *IP* -module NETTCPIP | more
get-NetiPcOnfiguration
```

## history
## Get History store history as long powershell window open 

```
get-history
invoke-history id <id no from get-history>
get-history | out-file <path for strore history>
```
#### Tracker keep track all the part your windows powershell session in text file it conatain all input and output get bu user 
```
help start-transcript
start-transcript -path <path>
```
#### stop transcipt
```
stop-transcript
```
## pipelining
## Pipelining use shadow copy

#### members (property and methods) of objects. mostly we are working with property
```
help get-member | more
get-member
```
```
get-service | select name, Status
get-service | select name, Status | out-file script_service.txt
get-service | where-object status -eq 'stopped' |format-list
```
## formatting

#### list format
```
help format-list
get-service | format-list | more
get-service | fl name,status | more
```
#### table format by defualt used
```
get-service | format-table -Autosize
get-service | format-table -wrap -Autosize
get-service | FT -wrap -autosize
```
#### gridview GUI format and also can do Slice(filter)
```
get-service | out-gridview
``` 
























