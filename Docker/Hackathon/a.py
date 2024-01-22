import os
import platform

def is_admin():
    system = platform.system().lower()
    
    if system == 'windows':
        try:
            # Check if the script is running with administrative privileges on Windows
            return os.getuid() == 0
        except AttributeError:
            try:
                # Check if the script is running with administrative privileges on Windows (alternative method)
                return os.system("NET SESSION >nul 2>&1") == 0
            except:
                return False

    elif system == 'linux' or system == 'darwin':
        # Check if the script is running with root privileges on Unix-like systems (Linux, macOS)
        return os.getuid() == 0

    else:
        # Unsupported operating system
        return False

if __name__ == "__main__":
    if is_admin():
        print(0)
    else:
        print(1)
