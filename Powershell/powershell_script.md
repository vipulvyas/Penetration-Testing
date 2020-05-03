
#### Powershell not run script by default so use following because set-Executionpolicy is seted restricted
```
help set-Executionpolicy
get-Executionpolicy
set-Executionpolicy Unrestricted
```

#### read and write on terminal
```
Read-Host "Enter Comp"
write-output "yeh"
```

#### parameter in script
```
param (
[Parameter(Mandatory=$true)][string]$ComputerName
)
```
#### foreach loop
```
Foreach ($a in $service)
{
 --- 
}
```
#### use property
```
using "." 
```



