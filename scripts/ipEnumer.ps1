

# $name = "Davood"

Write-Host("Welcome to Yakuza-Club Ninja ....")

$choose = Read-Host("Choosing by Number => 
[0]-All
[1]-Ping
[2]-Tracert
[3]-Curl
[4]-Port Scan
=> ") 

$ip = Read-Host("Enter Target IP")
#$password = Read-Host "Enter Your Password" -AsSecureString


if ($choose -eq 0){
    Write-Host("Pinging Start...")
    PING.EXE $ip

    Write-Host("Curl Start...")
    curl.exe "https://$ip"

    Write-Host("Trace Routing Start...")
    TRACERT.EXE "https://$ip"

    Write-Host("Nmap TCP Port Scan Start...")
    nmap.exe -A "$ip"

}elseif ($choose -eq 1){
    Write-Host("Pinging Start...")
    PING.EXE $ip

}elseif($choose -eq 2){
    Write-Host("Trace Routing Start...")
    TRACERT.EXE "https://$ip"

}elseif($choose -eq 3){
    Write-Host("Curl Start...")
    curl.exe "https://$ip"

}elseif($choose -eq 4){
    Write-Host("Nmap TCP Port Scan Start...")
    nmap.exe -A "$ip" --unprivileged
}

