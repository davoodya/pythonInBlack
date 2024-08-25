# ipEnumer.ps1
# Description: A PowerShell script for IP enumeration and network diagnostics
# Author: Yakuza.D
# Version: 2.0

Add-Type -AssemblyName Microsoft.VisualBasic

# Function to display help information
function Show-Help {
    $helpMessage = @"
Usage of Tool =>
    This tool performs various network operations based on user input.

Options:
[0]-All => Perform all operations (Ping, Trace Route, cURL, Port Scan, and System Information).
[1]-Ping => Ping the target IP.
[2]-Tracert => Perform a trace route to the target IP.
[3]-Curl => Perform a cURL request to the target IP.
[4]-Port Scan => Conduct a TCP port scan on the target IP using Nmap.
[5]-System Information => Display system information.
"@

    [Microsoft.VisualBasic.Interaction]::MsgBox($helpMessage, "OKOnly,Information", "Help Information")
}

# Welcome message
Write-Host("Welcome to Yakuza-Club Ninja ....") -BackgroundColor DarkMagenta -ForegroundColor White

# Get IP address from user
$ip = [Microsoft.VisualBasic.Interaction]::InputBox("Enter the target IP address:", "IP Address Input")

if ([string]::IsNullOrWhiteSpace($ip)) {
    [Microsoft.VisualBasic.Interaction]::MsgBox("No IP address entered. Exiting script.", "OKOnly,Critical", "Error")
    exit
}

# Get operation option from user
$optionInput = [Microsoft.VisualBasic.Interaction]::InputBox(
    "Enter the operation number (0-5):
    0: All operations
    1: Ping
    2: Trace Route
    3: cURL
    4: Port Scan
    5: System Information
    6: Help", 
    "Operation Selection")

if ([string]::IsNullOrWhiteSpace($optionInput)) {
    [Microsoft.VisualBasic.Interaction]::MsgBox("No option selected. Exiting script.", "OKOnly,Critical", "Error")
    exit
}

$option = [int]$optionInput

# Show help if option 6 is selected
if ($option -eq 6) {
    Show-Help
    exit
}

# Perform operations based on the selected option
switch ($option) {
    0 {
        Write-Host("All Operation Started but You be Wait More...") -BackgroundColor Yellow -ForegroundColor Black 
        Write-Host("Pinging Start...")  -ForegroundColor Yellow
        PING.EXE $ip
        Write-Host("Curl Start...")  -ForegroundColor Yellow
        curl.exe "https://$ip"
        Write-Host("Trace Routing Start...")  -ForegroundColor Yellow
        TRACERT.EXE "$ip"
        Write-Host("Nmap TCP Port Scan Start...")  -ForegroundColor Yellow
        gsudo.exe nmap.exe -A -sS -p- "$ip" --unprivileged
    }
    1 {
        Write-Host("Pinging Start...")  -ForegroundColor Yellow
        PING.EXE $ip
    }
    2 {
        Write-Host("Trace Routing Start...")  -ForegroundColor Yellow
        TRACERT.EXE "$ip"
    }
    3 {
        Write-Host("Curl Start...")  -ForegroundColor Yellow
        curl.exe "https://$ip"
    }
    4 {
        Write-Host("Nmap TCP Port Scan Start...")  -ForegroundColor Yellow
        gsudo.exe nmap.exe -A -p- "$ip" --unprivileged
    }
    5 {
        neofetch.cmd
    }
    default {
        [Microsoft.VisualBasic.Interaction]::MsgBox("Invalid option selected. Please run the script again and choose a valid option.", "OKOnly,Critical", "Error")
    }
}
