Get-Wmiobject -Class win32_OperatingSystem -ComputerName localhost
Select-Object -Property CSName,@{n=”Last Booted”;
e={[Management.ManagementDateTimeConverter]::ToDateTime($_.LastBootUpTime)}}