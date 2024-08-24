Add-Type -AssemblyName Microsoft.VisualBasic

$domain = [Microsoft.VisualBasic.Interaction]::InputBox("Whats Your Target domain???", "Enter domain...")

Write-Host($domain)
#Set-Location "E:\Softwares\00_Windows\Security\gobuster_Windows_i386"
[Microsoft.VisualBasic.Interaction]::MsgBox("Attacking Started...")
gobuster.exe dir -u $domain -w "H:\Repo\black_python\mini_projects\wordlists\dirlist_medium.txt"

[Microsoft.VisualBasic.Interaction]::MsgBox("Attacking Finished...")