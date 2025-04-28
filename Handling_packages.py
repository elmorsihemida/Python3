import subprocess
# ==============> Using run >=========================
def install_or_remove_packages():
    iOrR = ""
    while iOrR not in ("I", "R"):
        print("Would you like to install or remove packages? (I/R)")
        iOrR = input().upper()

    if iOrR == "I":
        action = "install"
    else:
        action = "remove"

    print("Enter a list of packages to install or remove")
    print("The list should be separated by spaces, for example:")
    print(" package1 package2 package3")
    print("Otherwise, input 'default' to", action, "the default packages listed in this program")

    packages = input().lower()
    if packages == "default":
        packages = "package1 package2 package3"  

    package_list = packages.split()

    if action == "install":
        subprocess.run(["sudo", "yum", "install", "-y"] + package_list)
    elif action == "remove":
        while True:
            print("Purge files after removing? (Y/N)")
            choice = input().upper()
            if choice == "Y":
                subprocess.run(["sudo", "yum", "--purge", "remove", "-y"] + package_list)
                break
            elif choice == "N":
                subprocess.run(["sudo", "yum", "remove", "-y"] + package_list)
                break

    subprocess.run(["sudo", "yum", "autoremove", "-y"])

install_or_remove_packages()

    