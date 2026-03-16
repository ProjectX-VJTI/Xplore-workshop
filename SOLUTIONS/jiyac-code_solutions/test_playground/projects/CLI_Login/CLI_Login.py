
# Created a CLI login/signup system 

import os
import time
import hashlib


# Created a function to clear screen
def clear_screen():
    time.sleep(1.5)
    os.system('cls' if os.name=='nt' else clear)


# Created a function to hash password
def hash(password):
    return hashlib.sha256(password.encode()).hexdigest()


# Created a function to register the user
def signup():
    check=False
    while not check:
        clear_screen()
        print("\n---Sign Up---")
        name=input("Enter your name: ")
        password=input("Enter your password: ")
        confirm=input("Confirm password: ")
        if(password==confirm):                          # If password does match confirm password, then the user is registered
            hashed_pass=hash(password)                  # Password is hashed and then stored
            with open("reg_users.txt","a") as f:
                f.write(name+","+hashed_pass+"\n")
            print("You have successfully registered.\n")
            check=True
        else:                                           
            print("Password does not match.\n")


# Created a function to login a registered user
def login():
    clear_screen()
    print("\n---Login---")
    name=input("Enter your name: ")
    password=input("Enter your password: ")
    hashed_pass=hash(password)                          # Password entered by user is hashed and compared with stored password

    with open("reg_users.txt", "r") as f:
        for line in f:
            stored_name, stored_pass=line.strip().split(",")
            if(stored_name==name and stored_pass==hashed_pass):
                print("You have successfully logged in!\n")
                clear_screen()
                print("Welcome",name)
                return True
  
    print("Could not find user. Please check your name and password or sign up first.")
    return False


def main():
    choice=0
    is_logged_in=False
    while choice !=3:
        if not is_logged_in:                                # Home Screen is displayed if user is not logged in
            clear_screen()
            print("\n---Home---")
            print(" 1. Login","\n","2. Sign Up","\n","3. Quit")
            choice=int(input("Enter your choice: "))
            match choice:
                case 1:
                    is_logged_in=login()
                case 2:
                    signup()
                case 3:
                    print("Goodbye")
                case _:
                    print("Invalid choice")
        else:                                               # Different screen shown when user is logged in
            print(" 1. Logout","\n","2. Quit")
            option=int(input("Enter your choice: "))
            match option:
                case 1:
                    is_logged_in=False                      # Back to Home screen
                case 2:
                    print("Goodbye")
                    choice=3                                # To exit program
                case _:
                    print("Invalid choice")

if __name__ == "__main__":
    main()
