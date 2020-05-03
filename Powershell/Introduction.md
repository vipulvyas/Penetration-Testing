# Introduction Of Powershell 

#### open ISE for scripting
```
ise
```



#### Power of Powershell csv file from all process from service manager not give proper readable output but powershell do it better and readable.all services running and stopped both.
```
get-service
```
#### stopped service <strong>where-object</strong> for condition
```
where-object Status -eq 'Stopped'
```

#### save in csv file 
```
export-csv path
```

#### combine all above
```
get-service | where-object Status -eq 'Stopped' | select-object Status, name, Displayname | export-csv path
```

