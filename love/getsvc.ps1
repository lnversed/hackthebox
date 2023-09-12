 $services = Get-ItemProperty -Path HKLM:\System\CurrentControlSet\Services\*  $services_tmp = $services | Where-Object {($_.ObjectName -eq "LocalSystem") -and ($_.Start -eq 3)}  $service_names = $services_tmp.pschildnameforeach ($name in $service_names){  
   $sddl = sc.exe sdshow $service_names -match "RP[A-Z]*?;;;AU"{ 
    $service_names  
    } 
}
