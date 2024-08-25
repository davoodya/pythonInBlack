# ipEnumer-GUI.ps1
# Description: A PowerShell script for IP enumeration, network diagnostics, and directory busting
# Author: Yakuza.D
# Version: 3.0

Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

# Set console color for better visibility
$host.UI.RawUI.BackgroundColor = "Black"
$host.UI.RawUI.ForegroundColor = "Green"
Clear-Host

# Function to display a custom message box
function Show-CustomMessageBox($message, $title, $icon = "Information") {
    $form = New-Object System.Windows.Forms.Form
    $form.Text = $title
    $form.Size = New-Object System.Drawing.Size(400,200)
    $form.StartPosition = "CenterScreen"

    $label = New-Object System.Windows.Forms.Label
    $label.Location = New-Object System.Drawing.Point(10,20)
    $label.Size = New-Object System.Drawing.Size(380,100)
    $label.Text = $message
    $form.Controls.Add($label)

    $okButton = New-Object System.Windows.Forms.Button
    $okButton.Location = New-Object System.Drawing.Point(150,120)
    $okButton.Size = New-Object System.Drawing.Size(100,30)
    $okButton.Text = "OK"
    $okButton.DialogResult = [System.Windows.Forms.DialogResult]::OK
    $form.Controls.Add($okButton)

    $form.AcceptButton = $okButton
    $form.TopMost = $true

    $form.ShowDialog() | Out-Null
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
    Write-Host "Welcome to Yakuza-Club Ninja ...." -BackgroundColor DarkMagenta -ForegroundColor White

    while ($true) {
        $optionForm = New-Object System.Windows.Forms.Form
        $optionForm.Text = "Operation Selection"
        $optionForm.Size = New-Object System.Drawing.Size(300,400)
        $optionForm.StartPosition = "CenterScreen"

        $optionLabel = New-Object System.Windows.Forms.Label
        $optionLabel.Location = New-Object System.Drawing.Point(10,20)
        $optionLabel.Size = New-Object System.Drawing.Size(280,30)
        $optionLabel.Text = "Select an operation:"
        $optionForm.Controls.Add($optionLabel)

        $optionListBox = New-Object System.Windows.Forms.ListBox
        $optionListBox.Location = New-Object System.Drawing.Point(10,50)
        $optionListBox.Size = New-Object System.Drawing.Size(260,250)
        $optionListBox.Items.AddRange(@("All operations", "Ping", "Trace Route", "cURL", "Port Scan", "System Information", "Directory Busting","V-Host Enumeration", "Help", "Exit"))
        $optionForm.Controls.Add($optionListBox)

        $okButton = New-Object System.Windows.Forms.Button
        $okButton.Location = New-Object System.Drawing.Point(100,310)
        $okButton.Size = New-Object System.Drawing.Size(100,30)
        $okButton.Text = "OK"
        $okButton.DialogResult = [System.Windows.Forms.DialogResult]::OK
        $optionForm.Controls.Add($okButton)

        $optionForm.AcceptButton = $okButton
        $optionForm.TopMost = $true

        $result = $optionForm.ShowDialog()

        if ($result -eq [System.Windows.Forms.DialogResult]::OK) {
            $option = $optionListBox.SelectedIndex
            if ($option -eq 8) {
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
                    #$targetIP = Get-IPAddress $target
                    Write-Host "Target: $target" -ForegroundColor Cyan
                    Write-Host "Target IP: $targetIP" -ForegroundColor Cyan
                    Write-Host "All Operations Started..." -BackgroundColor Yellow -ForegroundColor Black 
                    
                    PING.EXE $target
                    TRACERT.EXE $target
                    curl.exe $target
                    gsudo.exe nmap.exe -A -p- $target --unprivileged
                    neofetch.cmd
                    
                    
                    # ... (rest of case 0 operations)
                }
                1 {
                    $target = [Microsoft.VisualBasic.Interaction]::InputBox("Enter the target IP address:", "Ping Target Input")
                    if ([string]::IsNullOrWhiteSpace($target)) {
                        throw "No target entered. Exiting script."
                    }
                    Write-Host "Pinging Start..." -ForegroundColor Yellow
                    PING.EXE $target
                }
                2 {
                    $target = [Microsoft.VisualBasic.Interaction]::InputBox("Enter the target IP address:", "Trace Route Target Input")
                    if ([string]::IsNullOrWhiteSpace($target)) {
                        throw "No target entered. Exiting script."
                    }
                    Write-Host "Trace Routing Start..." -ForegroundColor Yellow
                    TRACERT.EXE $target
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
                    $target = [Microsoft.VisualBasic.Interaction]::InputBox("Enter the target URL (with https://):", "V-Host Enumeration Target Input")
                    if ([string]::IsNullOrWhiteSpace($target)) {
                        throw "No target entered. Exiting script."
                    }
                    if (Test-ToolInstalled "gobuster") {
                        Write-Host "V-Host Enumeration Start..." -ForegroundColor Yellow
                        $defaultWordlist = "H:\Repo\black_python\mini_projects\wordlists\vhost-wordlist.txt"
                        $customWordlist = [Microsoft.VisualBasic.Interaction]::InputBox("Enter the path to the wordlist (leave empty for default):", "Wordlist Selection")
                        
                        $wordlist = if ([string]::IsNullOrWhiteSpace($customWordlist)) { $defaultWordlist } else { $customWordlist }
                        
                        if (Test-Path $wordlist) {
                            gobuster.exe vhost -u $target -w $wordlist
                        } else {
                            throw "Wordlist file not found: $wordlist"
                        }
                    } else {
                        throw "Gobuster is not installed. Please install Gobuster and try again."
                    }
                }
                8 {
                    Show-Help
                }
                default {
                    throw "Invalid option selected. Please run the script again and choose a valid option."
                }
            }

                    #Show-CustomMessageBox "Operations completed successfully!" "Success"

        }
        else
        {
            break
        }
    }
    Show-CustomMessageBox "Operations completed successfully!" "Success"
}
catch {
    Write-Host "An error occurred: $_" -ForegroundColor Red
    Show-CustomMessageBox "An error occurred: $_" "Error" "Error"
}

finally {
    # Reset console colors
    $host.UI.RawUI.BackgroundColor = $host.UI.RawUI.OriginalBackgroundColor
    $host.UI.RawUI.ForegroundColor = $host.UI.RawUI.OriginalForegroundColor
    Clear-Host
}

