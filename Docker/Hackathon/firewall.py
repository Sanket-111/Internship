import subprocess

def is_firewall_enabled():
    try:
        # Run a command to check if the Windows Firewall service is running
        result = subprocess.run(["sc", "query", "MpsSvc"], capture_output=True, text=True)

        # Check if the output contains "RUNNING"
        return "RUNNING" in result.stdout.upper()

    except Exception as e:
        print(f"Error checking firewall status: {e}")
        return None

if __name__ == "__main__":
    firewall_enabled = is_firewall_enabled()
    
    if firewall_enabled is not None:
        if firewall_enabled:
            print("Firewall is enabled.")
        else:
            print("Firewall is not enabled.")
    else:
        print("Unable to determine firewall status.")
