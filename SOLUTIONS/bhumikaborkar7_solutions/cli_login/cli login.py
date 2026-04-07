#cli login signup system 
import os
import hashlib
FILE= "data.txt"
is_logged_in= False
user=None

def clr(): #func clears the terminal
    os.system('cls' if os.name=="nt" else 'clear')
    
def hashpassword(password):  #converts the password to hashed form
    return hashlib.sha256(password.encode()).hexdigest()

def signup():
    clr()
    print("SIGNUP")
    username=input("enter name:").strip()
    password1=input("enter password:").strip()
    if username == "" or password1 == "":
        print("Username and password cannot be empty!")
        input("press enter to continue")
        return
    alldigits=True
    for ch in username:
        if ch<'0' or ch>'9':
            alldigits=False
            break
    if alldigits:
        print("username cannot be only numbers")
        input("press enter to continue")
        return
    hashed=hashpassword(password1)
    with open(FILE, "a") as f:
        f.write(f"{username},{hashed}\n")
    print("signup successful")
    input("press enter to continue")

def login():
    global is_logged_in, user
    clr()
    print("login")
    username=input("enter name:").strip()
    password1=input("enter password:").strip()
    hashed=hashpassword(password1)
    try:
        with open(FILE, "r") as f:
            for line in f:
                x, y= line.strip().split(",")
                if x==username and y==hashed:
                    is_logged_in=True
                    user=username
                    print("login successful")
                    input("press enter")
                    return
    except FileNotFoundError:
        pass
    print("invalid username or password")
    input("press enter to continue")

def welcome():
    clr()
    print(f"welcome, {user}")
    print("1. logout\n2. exit")
    choice=input("choose:")
    global is_logged_in
    match choice:            #match case for welcome windows page
        case "1": 
            is_logged_in=False
        case "2":
            exit()
        case _:
            print("invalid choice")
            input("press enter to continue")

def main():
    while True:
        if is_logged_in:
            welcome()
        else:
            clr()
            print("MAIN MENU")
            print("1. login\n2. signup\n3. exit")
            choice=input("enter a valid choice:")
            match choice:         #match case for login, signup
                case "1":
                    login()
                case "2":
                    signup()
                case "3":
                    break
                case _:
                    print("invalid choice")
                    input("press enter to continue")

if __name__ == "__main__":
    main()

