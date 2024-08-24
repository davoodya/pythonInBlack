# ipEnumer-GUI.ps1
# Description: A PowerShell script for IP enumeration, network diagnostics, and directory busting
# Author: Yakuza.D
# Version: 3.0

Add-Type -AssemblyName Microsoft.VisualBasic
Add-Type -AssemblyName System.Windows.Forms

# Set console color for better visibility
$host.UI.RawUI.BackgroundColor = "Black"
$host.UI.RawUI.ForegroundColor = "Green"
Clear-Host

# Function to display a custom message box
function Show-CustomMessageBox($message, $title, $icon = "Information") {
    [System.Windows.Forms.MessageBox]::Show($message, $title, [System.Windows.Forms.MessageBoxButtons]::OK, [System.Windows.Forms.MessageBoxIcon]::$icon)
}

# Function to check if a tool is installed
function Test-ToolInstalled($toolName) {
    try {
        $null = Get-Command $toolName -ErrorAction Stop
        return $true
    }
    catch {
        return $false
    }
}

# Function to display help information
function Show-Help {
    $helpMessage = @"
Usage of Tool =>
    This tool performs various network operations based on user input.

Options:
[0]-All => Perform all operations (Ping, Trace Route, cURL, Port Scan, System Information, and Directory Busting).
[1]-Ping => Ping the target IP.
[2]-Tracert => Perform a trace route to the target IP.
[3]-Curl => Perform a cURL request to the target IP.
[4]-Port Scan => Conduct a TCP port scan on the target IP using Nmap.
[5]-System Information => Display system information.
[6]-Directory Busting => Perform directory busting using Gobuster.
[7]-Help => Display this help information.
"@

    Show-CustomMessageBox $helpMessage "Help Information"
}
# Main script logic
try {
    # Welcome message
     # Welcome message
     Write-Host "Welcome to Yakuza-Club Ninja ...." -BackgroundColor DarkMagenta -ForegroundColor White

     while ($true) {
         # Get operation option from user
         $optionInput = [Microsoft.VisualBasic.Interaction]::InputBox(
             "Enter the operation number (0-7, 99 to exit):
             0: All operations
             1: Ping
             2: Trace Route
             3: cURL
             4: Port Scan
             5: System Information
             6: Directory Busting
             7: Help
             99: Exit", 
             "Operation Selection")
 
         if ([string]::IsNullOrWhiteSpace($optionInput)) {
             throw "No option selected. Exiting script."
         }
 
         $option = [int]$optionInput
 
         if ($option -eq 99) {
             Write-Host "Exiting the program. Goodbye!" -ForegroundColor Cyan
             break
         }
 
    # Perform operations based on the selected option
    switch ($option) {
        0 {
            $target = [Microsoft.VisualBasic.Interaction]::InputBox("Enter the target IP address or domain(with https://):", "Target Input")
            if ([string]::IsNullOrWhiteSpace($target)) {
                throw "No target entered. Exiting script."
            }
            $targetIP = Get-IPAddress $target
            Write-Host "Target: $target" -ForegroundColor Cyan
            Write-Host "Target IP: $targetIP" -ForegroundColor Cyan

            Write-Host "All Operations Started..." -BackgroundColor Yellow -ForegroundColor Black 
            
            # ... (rest of case 0 operations)
        }
        1 {
            $target = [Microsoft.VisualBasic.Interaction]::InputBox("Enter the target IP address or domain:", "Ping Target Input")
            if ([string]::IsNullOrWhiteSpace($target)) {
                throw "No target entered. Exiting script."
            }
            Write-Host "Pinging Start..." -ForegroundColor Yellow
            $pingTarget = $target -replace '^https?://', ''
            PING.EXE $pingTarget
        }
        2 {
            $target = [Microsoft.VisualBasic.Interaction]::InputBox("Enter the target IP address or domain:", "Trace Route Target Input")
            if ([string]::IsNullOrWhiteSpace($target)) {
                throw "No target entered. Exiting script."
            }
            $targetIP = Get-IPAddress $target
            Write-Host "Trace Routing Start..." -ForegroundColor Yellow
            TRACERT.EXE $targetIP
        }
        3 {
            $target = [Microsoft.VisualBasic.Interaction]::InputBox("Enter the target URL (with https://):", "cURL Target Input")
            if ([string]::IsNullOrWhiteSpace($target)) {
                throw "No target entered. Exiting script."
            }
            Write-Host "Curl Start..." -ForegroundColor Yellow
            curl.exe $target
        }
        4 {
            $target = [Microsoft.VisualBasic.Interaction]::InputBox("Enter the target IP address or domain:", "Port Scan Target Input")
            if ([string]::IsNullOrWhiteSpace($target)) {
                throw "No target entered. Exiting script."
            }
            if (Test-ToolInstalled "nmap") {
                Write-Host "Nmap TCP Port Scan Start..." -ForegroundColor Yellow
                gsudo.exe nmap.exe -A -p- $target --unprivileged
            } else {
                throw "Nmap is not installed. Please install Nmap and try again."
            }
        }
        5 {
            Write-Host "System Information:" -ForegroundColor Yellow
            neofetch.cmd
        }
        6 {
            $target = [Microsoft.VisualBasic.Interaction]::InputBox("Enter the target URL (with https://):", "Directory Busting Target Input")
            if ([string]::IsNullOrWhiteSpace($target)) {
                throw "No target entered. Exiting script."
            }
            if (Test-ToolInstalled "gobuster") {
                Write-Host "Directory Busting Start..." -ForegroundColor Yellow
                $defaultWordlist = "H:\Repo\black_python\mini_projects\wordlists\directory-list-2.3-small.txt"
                $customWordlist = [Microsoft.VisualBasic.Interaction]::InputBox("Enter the path to the wordlist (leave empty for default):", "Wordlist Selection")
                
                $wordlist = if ([string]::IsNullOrWhiteSpace($customWordlist)) { $defaultWordlist } else { $customWordlist }
                
                if (Test-Path $wordlist) {
                    gobuster.exe dir -u $target -w $wordlist
                } else {
                    throw "Wordlist file not found: $wordlist"
                }
            } else {
                throw "Gobuster is not installed. Please install Gobuster and try again."
            }
        }
        7 {
            Show-Help
        }
        default {
            throw "Invalid option selected. Please run the script again and choose a valid option."
        }
    }

    Show-CustomMessageBox "Operations completed successfully!" "Success"
}
catch {
    Write-Host "An error occurred: $_" -ForegroundColor Red
    Show-CustomMessageBox "An error occurred: $_" "Error" "Error"
}

}
finally {
    # Reset console colors
    $host.UI.RawUI.BackgroundColor = $host.UI.RawUI.OriginalBackgroundColor
    $host.UI.RawUI.ForegroundColor = $host.UI.RawUI.OriginalForegroundColor
    Clear-Host
}

