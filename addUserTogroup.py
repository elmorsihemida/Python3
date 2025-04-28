# add user to group Using peopen
import subprocess

def add_user_to_group(username,groupname):
    try:

        command = ['sudo','usermod','-aG',groupname,username]

        # Using peopen commmand

        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()

    #التحقق من نجاح العمليه
        if process.returncode ==0:
            print(f"user {username} added to group {groupname} successfully")
        else:
            print(f"Failed to add user {username} to group {groupname}")
            print("Error:", error.decode())

    except Exception as e:
        print(f"An Error occured: {str(e)}")

user = input("Enter username: ")
group = input("enter group name: ")
add_user_to_group(user,group)
