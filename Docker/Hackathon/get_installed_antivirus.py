import wmi

def get_installed_antivirus():
    try:
        c = wmi.WMI()

        # Query for antivirus products
        antivirus_products = c.Win32_Product(Description="Antivirus")

        if antivirus_products:
            return [product.Name for product in antivirus_products]
        else:
            return []

    except Exception as e:
        print(f"Error checking antivirus status: {e}")
        return None

if __name__ == "__main__":
    installed_antivirus = get_installed_antivirus()
    
    if installed_antivirus is not None and installed_antivirus:
        # print("Installed antivirus software:")
        # for antivirus in installed_antivirus:
        #     print(f"- {antivirus}")
        print(0)
    else:
        print(1)
