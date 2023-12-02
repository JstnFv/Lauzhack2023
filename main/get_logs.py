import subprocess

def log_system_events(days):
    try:
        # PowerShell command to get system events from the last week and convert to JSON
        powershell_command = f'''
            Get-EventLog -LogName System -After (Get-Date).AddDays(-{days}) |
            Select-Object TimeGenerated, EntryType, Source, Message |
            ConvertTo-Json |
            Out-File -FilePath system_logs_last_{days}_days.json
        '''
        result = subprocess.run(['powershell', '-Command', powershell_command], capture_output=True, text=True, check=True)

        print(f"System logs from the last {days} days successfully captured and saved to system_logs_last_{days}_days.json.")
    except subprocess.CalledProcessError as e:
        print(f"Error capturing system logs: {e}")
        print(f"PowerShell stderr: {e.stderr.decode('utf-8')}")

# Call the function to log system events for the last 7 days
log_system_events("30")
