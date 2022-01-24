from cryptography.fernet import Fernet
import key_generator

def load_key():
    f= open("key.key",'rb')
    key = f.read()
    f.close()
    return key

key=load_key() + master_pwd.encode()
fer = Fernet(key)

def view():
    print("\n")
    with open('passwords.txt','r') as f:
        for line in f.readlines():
            line=line.rstrip()
            line=line.split("|")
            usern = line[0]
            pwd = ''.join(line[1:])
            print("User: "+ line[0] + ", Password: "+ fer.decrypt(pwd.encode()).decode())

def add():
    name = input("\nEnetr the username: ")
    pwd = input("Enter your password: ")
    with open('passwords.txt','a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode= input("\nWould you like to add a new password or view the existing ones (view,add) ?\nPress q to quit : ").lower()
    if mode=='q':
        break

    if mode=='view':
        view()
    elif mode=='add':
        add()       
    else:
        print("Invalid mode")