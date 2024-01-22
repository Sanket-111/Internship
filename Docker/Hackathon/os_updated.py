import subprocess
import platform

def is_os_updated_windows():
    try:
        result = subprocess.run(["powershell", "Get-HotFix"], capture_output=True, text=True)
        return "Update" in result.stdout
    except Exception as e:
        print(f"Error checking Windows update status: {e}")
        return None

def is_os_updated_linux():
    try:
        result = subprocess.run(["sudo", "apt", "list", "--upgradable"], capture_output=True, text=True)
        return "upgradable" in result.stdout
    except Exception as e:
        print(f"Error checking Linux update status: {e}")
        return None
    
def is_os_updated_macos():
    try:
        result = subprocess.run(["softwareupdate", "-l"], capture_output=True, text=True)
        return "No new software available." not in result.stdout
    except Exception as e:
        print(f"Error checking macOS update status: {e}")
        return None
    
def get_os_name():
    return platform.system()

if __name__ == "__main__":

    os_name = get_os_name()

    if os_name == "Windows":
        os_updated = is_os_updated_windows()
    
    elif os_name == "Linux":
        os_updated = is_os_updated_linux()
    
    else :
        os_updated = is_os_updated_macos()
        
    print(os_name)
    
    if os_updated is not None:
        if os_updated:
            print("The operating system is updated.")
        else:
            print("The operating system is not updated.")
    else:
        print("Unable to determine update status.")