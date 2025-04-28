# adding user using os module

import os
def new_user():
    confirm = "N"
    while confirm != "Y":
        username = input("Enter the name od the user to add: ")
        print("Use the username '" + username + "'? (Y/N) ")
        confirm = input().upper()
    os.system("sudo adduser -r " + username)
