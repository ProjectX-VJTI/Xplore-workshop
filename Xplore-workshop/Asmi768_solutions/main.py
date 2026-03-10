"""
Project: CLI Authentication System
Author: Asmi Mohan
Description:
A simple command-line authentication system
that allows users to register and login.
"""

# ---------------------------------------
# Function: Register a new user
# ---------------------------------------
def register():
    print("\n--- Register ---")

    username = input("Enter username: ")
    password = input("Enter password: ")

    # Save user credentials in file
    with open("users.txt", "a") as file:
        file.write(username + "," + password + "\n")

    print("User registered successfully!\n")


# ---------------------------------------
# Function: Login existing user
# ---------------------------------------
def login():
    print("\n--- Login ---")

    username = input("Enter username: ")
    password = input("Enter password: ")

    try:
        with open("users.txt", "r") as file:
            users = file.readlines()

        for user in users:
            stored_username, stored_password = user.strip().split(",")

            if username == stored_username and password == stored_password:
                print("Login successful!\n")
                return

        print("Invalid credentials!\n")

    except FileNotFoundError:
        print("No users registered yet.\n")


# ---------------------------------------
# Main Menu Controller
# ---------------------------------------
def main():
    while True:
        print("====== CLI AUTH SYSTEM ======")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid option. Try again.\n")


# ---------------------------------------
# Program Entry Point
# ---------------------------------------
if __name__ == "__main__":
    main()