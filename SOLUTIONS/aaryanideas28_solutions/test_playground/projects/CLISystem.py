import hashlib
import os
import tkinter as tk
from tkinter import messagebox

def get_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

def handle_gui_signup(u_input, p_input):
    user = u_input.get()
    pwd = p_input.get()
    if user and pwd:
        with open("users.txt", "a") as file:
            file.write(f"{user},{get_hash(pwd)}\n")
        messagebox.showinfo("Success", "Signup successful!")
    else:
        messagebox.showwarning("Error", "Fields cannot be empty")

def handle_gui_login(u_input, p_input):
    user = u_input.get()
    pwd = p_input.get()
    hashed_pwd = get_hash(pwd)
    try:
        with open("users.txt", "r") as file:
            for line in file:
                stored_user, stored_hash = line.strip().split(",")
                if user == stored_user and hashed_pwd == stored_hash:
                    messagebox.showinfo("Success", f"Welcome, {user}!")
                    return
        messagebox.showerror("Error", "Invalid credentials")
    except FileNotFoundError:
        messagebox.showerror("Error", "No users found")

def launch_gui():
    root = tk.Tk()
    root.title("Healthcare Login - GUI Mode")
    root.geometry("300x200")
    
    tk.Label(root, text="Username:").pack()
    u_input = tk.Entry(root)
    u_input.pack()
    
    tk.Label(root, text="Password:").pack()
    p_input = tk.Entry(root, show="*")
    p_input.pack()
    
    tk.Button(root, text="Login", command=lambda: handle_gui_login(u_input, p_input)).pack(pady=5)
    tk.Button(root, text="Signup", command=lambda: handle_gui_signup(u_input, p_input)).pack()
    
    root.mainloop()

def cli_signup():
    user = input("Enter new username: ")
    pwd = input("Enter new password: ")
    with open("users.txt", "a") as file:
        file.write(f"{user},{get_hash(pwd)}\n")
    print("Signup successful!")

def cli_login():
    user = input("Username: ")
    pwd = input("Password: ")
    hashed_pwd = get_hash(pwd)
    try:
        with open("users.txt", "r") as file:
            for line in file:
                stored_user, stored_hash = line.strip().split(",")
                if user == stored_user and hashed_pwd == stored_hash:
                    return True
        return False
    except FileNotFoundError:
        return False

print("Choose Interface Mode:")
print("1. CLI (Terminal)")
print("2. GUI (Window)")
mode = input("Select (1/2): ")

if mode == "1":
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1. Login\n2. Signup\n3. Exit")
        choice = input("Select: ")
        match choice:
            case "1":
                if cli_login():
                    print("Welcome!")
                    input("Press Enter to logout...")
                else:
                    print("Login failed.")
                    input("Press Enter to try again...")
            case "2":
                cli_signup()
            case "3":
                break
elif mode == "2":
    launch_gui()