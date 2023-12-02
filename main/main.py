import subprocess

def log_system_events():
    try:
        # Run corrected PowerShell command to get system events from the last week
        powershell_command = 'Get-EventLog -LogName System -After (Get-Date).AddDays(-7) | Out-File -Append -FilePath system_logs.txt'
        result = subprocess.run(['powershell', '-Command', powershell_command], capture_output=True, text=True, check=True)

        print("System logs from the past week successfully captured.")
    except subprocess.CalledProcessError as e:
        print(f"Error capturing system logs: {e}")
        print(f"PowerShell stderr: {e.stderr.decode('utf-8')}")

# Call the function to log system events
log_system_events()
