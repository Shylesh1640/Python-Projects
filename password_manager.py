from os import write
from cryptography.fernet import Fernet

master_pwd = input("What is the master password? ")



def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key()

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            name, pwd = data.split("|")
            print("Account:", name, ", Password:", pwd)
            
        
def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    with open("passwords.txt", "a") as f:
        f.write(name + "|" + pwd + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones? (add/view),press q to quit ").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
        
        

