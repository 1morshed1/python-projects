
from cryptography.fernet import Fernet

'''
The code snippet below is used to generate key

def write_key():
    key = Fernet.generate_key()
    with open("G:\\python-projects\\password-manager\\key.key", "wb") as key_file:
        key_file.write(key)
'''

def load_key():
    file = open("G:\\python-projects\\password-manager\\key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()

master_pwd = input("What is the master password? ")


def view():
    with open("G:\\python-projects\\password-manager\\passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:",user,", Password: ", passw)

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("G:\\python-projects\\password-manager\\passwords.txt", "a") as f:
        f.write(name + "|" + pwd + "\n")

while True:
    mode  = input("Would you like to add a new password or view existing ones (view, add)? Press q to quit. ").lower()

    if mode == "q":
        break

    if mode == "view":
        view()

    elif mode == "add":
        add()

    else:
        print("Invalid Mode.")
        continue

