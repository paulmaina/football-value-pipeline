# Run once from the repository folder. Keys stay in the local .env.
$ErrorActionPreference = 'Stop'
$repoPath = Split-Path -Parent $MyInvocation.MyCommand.Path
$pythonLauncher = (Get-Command py -ErrorAction Stop).Source
$action = New-ScheduledTaskAction -Execute $pythonLauncher -Argument ('"' + (Join-Path $repoPath 'closing_odds.py') + '" --max-requests 100') -WorkingDirectory $repoPath
$trigger = New-ScheduledTaskTrigger -Once -At (Get-Date).AddMinutes(1) -RepetitionInterval (New-TimeSpan -Minutes 1)
$settings = New-ScheduledTaskSettingsSet -MultipleInstances IgnoreNew -ExecutionTimeLimit (New-TimeSpan -Minutes 4) -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries
$principal = New-ScheduledTaskPrincipal -UserId ([System.Security.Principal.WindowsIdentity]::GetCurrent().Name) -LogonType Interactive -RunLevel Limited
Register-ScheduledTask -TaskName 'FootballClosingOddsCollector' -Action $action -Trigger $trigger -Settings $settings -Principal $principal -Description 'Local pre-kickoff quotes; .env keys; requires signed-in user and awake computer; no bets or Git pushes.' -Force | Out-Null
Write-Host 'Collector registered. Keep this computer awake and signed in around kickoff. Push collected quote files using your normal Git workflow.'
