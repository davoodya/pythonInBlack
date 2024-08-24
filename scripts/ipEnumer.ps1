# ipEnumer.ps1
# Description: A PowerShell script for IP enumeration and network diagnostics
# Author: Yakuza.D
# Version: 1.0

# Define script parameters
param (
    [string]$ip, # Target IP address
    [int]$option, # Operation option
    [switch]$help # Help flag
)

# Display help information if -help switch is used
if ($help) {
    Write-Host "Usage of Tool =>" -ForegroundColor Yellow
    Write-Host "    .\ipEnumer.ps1 -ip <Target-Ip> -option <Option-Number>" -ForegroundColor White
    Write-Host ""

    Write-Host "Description:" -ForegroundColor Yellow
    Write-Host "--------====****====-------" -ForegroundColor DarkCyan

    Write-Host "-ip <Target-Ip>:" -ForegroundColor Cyan -NoNewline
    Write-Host " Specifies the target IP address on which the selected operation will be performed." -ForegroundColor White

    Write-Host "-option <Option-Number>:" -ForegroundColor Cyan -NoNewline
    Write-Host " Specifies the operation to perform. The following options are available:" -ForegroundColor White

    Write-Host "-help:" -ForegroundColor Cyan -NoNewline
    Write-Host " Displays the usage guide with details about the available options and exits the script." -ForegroundColor White

    Write-Host ""

    Write-Host "Options:" -ForegroundColor Yellow
    Write-Host "--------====****====-------" -ForegroundColor DarkCyan

    Write-Host "[0]-All => " -ForegroundColor Green -NoNewline
    Write-Host "Perform all operations (Ping, Trace Route, cURL, Port Scan, and System Information)." -ForegroundColor White

    Write-Host "[1]-Ping => " -ForegroundColor Green -NoNewline
    Write-Host "Ping the target IP." -ForegroundColor White

    Write-Host "[2]-Tracert => " -ForegroundColor Green -NoNewline
    Write-Host "Perform a trace route to the target IP." -ForegroundColor White

    Write-Host "[3]-Curl => " -ForegroundColor Green -NoNewline
    Write-Host "Perform a cURL request to the target IP." -ForegroundColor White

    Write-Host "[4]-Port Scan => " -ForegroundColor Green -NoNewline
    Write-Host "Conduct a TCP port scan on the target IP using Nmap." -ForegroundColor White

    Write-Host "[5]-System Information => " -ForegroundColor Green -NoNewline
    Write-Host "Display system information." -ForegroundColor White

    Write-Host ""

    Write-Host "Examples:" -ForegroundColor Yellow
    Write-Host "--------====****====-------" -ForegroundColor DarkCyan

    Write-Host "Execute All Operations =>" -ForegroundColor Magenta
    Write-Host "    .\ipEnumer.ps1 -ip 192.168.1.1 -option 0" -ForegroundColor White
    Write-Host "------------------" -ForegroundColor DarkGray

    Write-Host "Ping an IP Address =>" -ForegroundColor Magenta
    Write-Host "    .\ipEnumer.ps1 -ip 192.168.1.1 -option 1" -ForegroundColor White
    Write-Host "------------------" -ForegroundColor DarkGray

    Write-Host "Trace Route to an IP Address =>" -ForegroundColor Magenta
    Write-Host "    .\ipEnumer.ps1 -ip 192.168.1.1 -option 2" -ForegroundColor White
    Write-Host "------------------" -ForegroundColor DarkGray

    Write-Host "Perform a cURL Request =>" -ForegroundColor Magenta
    Write-Host "    .\ipEnumer.ps1 -ip 192.168.1.1 -option 3" -ForegroundColor White
    Write-Host "-----------------" -ForegroundColor DarkGray

    Write-Host "TCP Port Scan =>" -ForegroundColor Magenta
    Write-Host "    .\ipEnumer.ps1 -ip 192.168.1.1 -option 4" -ForegroundColor White
    Write-Host "------------------" -ForegroundColor DarkGray

    Write-Host "Display Help Message =>" -ForegroundColor Magenta
    Write-Host "    .\ipEnumer.ps1 -help" -ForegroundColor White 
    exit
}
# Welcome message
Write-Host("Welcome to Yakuza-Club Ninja ....") -BackgroundColor DarkMagenta -ForegroundColor White

# Perform operations based on the selected option
if ($option -eq 0){
    Write-Host("All Operation Started but You be Wait More...") -BackgroundColor Yellow -ForegroundColor Black 

    # Option 0: Perform all operations
    Write-Host("Pinging Start...")  -ForegroundColor Yellow
    PING.EXE $ip

    Write-Host("Curl Start...")  -ForegroundColor Yellow
    curl.exe "https://$ip"

    Write-Host("Trace Routing Start...")  -ForegroundColor Yellow
    TRACERT.EXE "$ip"

    Write-Host("Nmap TCP Port Scan Start...")  -ForegroundColor Yellow
    gsudo.exe nmap.exe -A -sS -p- "$ip" --unprivileged

}elseif ($option -eq 1){
    # Option 1: Ping the target IP
    Write-Host("Pinging Start...")  -ForegroundColor Yellow
    PING.EXE $ip

}elseif($option -eq 2){
    # Option 2: Perform trace route
    Write-Host("Trace Routing Start...")  -ForegroundColor Yellow
    TRACERT.EXE "$ip"

}elseif($option -eq 3){
    # Option 3: Perform cURL request
    Write-Host("Curl Start...")  -ForegroundColor Yellow

    curl.exe "https://$ip"

}elseif($option -eq 4){
    # Option 4: Perform Nmap TCP port scan
    Write-Host("Nmap TCP Port Scan Start...")  -ForegroundColor Yellow
    gsudo.exe nmap.exe -A -p- "$ip" --unprivileged
    # Commented out alternative command:
    #nmap.exe -A "$ip" --unprivileged

}elseif ($option -eq 5) {
    # Option 5: Display system information using neofetch
    neofetch.cmd
}

