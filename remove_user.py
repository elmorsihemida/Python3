#remove User Using a function 
import os
def del_user():
    confirm = "N"
    while confirm != "Y":
        username = input("Enter username to delete: ")
        print("Are you Sure, delete: "+username+" ?(Y/N)")
        confirm = input.upper()
    os.system("sudo userdel -r "+ username)

#calling  function to del_user

del_user()