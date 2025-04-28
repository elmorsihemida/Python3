import subprocess
#add user to group using (subprocess.run)
def add_user_to_group(username,groupname):
    try:
        command = ['sudo','usermod','-aG',groupname,username]
        subprocess.run(command,check=True)
        print(f"User {username} added to group {groupname} Sucessfully")

    except subprocess.CalledProcessError:
        print(f"Failed to add user {username} to group {groupname}")

user = input("Enter username: ")
group = input("enter group name: ")
add_user_to_group(user,group)