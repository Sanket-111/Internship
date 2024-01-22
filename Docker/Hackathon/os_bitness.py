import platform

def get_os_bitness():
    bits, linkage = platform.architecture()
    return bits

if __name__ == "__main__":
    os_bitness = get_os_bitness()
    print(f"The operating system bitness is: {os_bitness}")
