# Import required assemblies
Add-Type -AssemblyName Microsoft.VisualBasic
Add-Type -AssemblyName System.Windows.Forms

# Set console color for better visibility
$host.UI.RawUI.BackgroundColor = "Black"
$host.UI.RawUI.ForegroundColor = "Green"
Clear-Host

# Function to display a custom message box
function Show-CustomMessageBox($message, $title) {
    [System.Windows.Forms.MessageBox]::Show($message, $title, [System.Windows.Forms.MessageBoxButtons]::OK, [System.Windows.Forms.MessageBoxIcon]::Information)
}

# Function to check if Gobuster is installed
function Test-GobusterInstalled {
    try {
        $null = Get-Command gobuster.exe -ErrorAction Stop
        return $true
    }
    catch {
        return $false
    }
}

# Main script logic
try {
    # Check if Gobuster is installed
    if (-not (Test-GobusterInstalled)) {
        throw "Gobuster is not installed or not in the system PATH. Please install Gobuster and try again."
    }

    # Get target domain from user
    $domain = [Microsoft.VisualBasic.Interaction]::InputBox("Enter your target domain:", "Domain Input")

    if ([string]::IsNullOrWhiteSpace($domain)) {
        throw "No domain entered. Exiting script."
    }

    Write-Host "Target domain: $domain" -ForegroundColor Cyan

    # Confirm attack initiation
    $confirmation = [System.Windows.Forms.MessageBox]::Show(
        "Are you sure you want to start the attack on $domain?",
        "Confirm Attack",
        [System.Windows.Forms.MessageBoxButtons]::YesNo,
        [System.Windows.Forms.MessageBoxIcon]::Warning
    )

    if ($confirmation -eq 'Yes') {
        Show-CustomMessageBox "Attack Started..." "Gobuster"

        # Run Gobuster
        $wordlist = "H:\Repo\black_python\mini_projects\wordlists\dirlist_medium.txt"
        if (-not (Test-Path $wordlist)) {
            throw "Wordlist file not found: $wordlist"
        }

        Write-Host "Running Gobuster..." -ForegroundColor Yellow
        gobuster.exe dir -u $domain -w $wordlist

        Show-CustomMessageBox "Attack Finished!" "Gobuster"
    }
    else {
        Write-Host "Attack cancelled by user." -ForegroundColor Yellow
    }
}
catch {
    Write-Host "An error occurred: $_" -ForegroundColor Red
    Show-CustomMessageBox "An error occurred: $_" "Error"
}
finally {
    # Reset console colors
    $host.UI.RawUI.BackgroundColor = $host.UI.RawUI.OriginalBackgroundColor
    $host.UI.RawUI.ForegroundColor = $host.UI.RawUI.OriginalForegroundColor
    Clear-Host
}
