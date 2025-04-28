# install or remove packages using peopen
import subprocess

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
        process = subprocess.Popen(["sudo", "apt-get", "install", "-y"] + package_list)
        process.communicate()  

    elif action == "remove":
        while True:
            print("Purge files after removing? (Y/N)")
            choice = input().upper()
            if choice == "Y":
                process = subprocess.Popen(["sudo", "apt-get", "--purge", "remove", "-y"] + package_list)
                process.communicate()
                break
            elif choice == "N":
                process = subprocess.Popen(["sudo", "apt-get", "remove", "-y"] + package_list)
                process.communicate()
                break

    cleanup = subprocess.Popen(["sudo", "apt", "autoremove", "-y"])
    cleanup.communicate()

install_or_remove_packages()
