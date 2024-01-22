import platform

def get_os_name():
    return platform.system()

if __name__ == "__main__":
    os_name = get_os_name()
    print(f"The operating system is: {os_name}")
