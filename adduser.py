import os

def new_user():
    confirm = "N"
    while confirm != "Y":
        username = input("Enter the name of the user: ")
        print(f"use the username {username}? (Y/N)")
        confirm = input().upper()
    os.system(f"sudo adduser {username}")
    
new_user()