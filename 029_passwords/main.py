import tkinter as tk
from tkinter import messagebox
import random
import string
import json

class PasswordManager:
    PASSWORD_LENGTH = 12
    COLUMN_WIDTH = 18
    PADX = 40
    PADY = 40

    def __init__(self, master):
        self.master = master
        self.master.title("Password Manager")
        self.master.config(padx=self.PADX, pady=self.PADY)
        self.setup_ui()

    def setup_ui(self):
        self.logo_img = tk.PhotoImage(file="logo.png")
        self.canvas = tk.Canvas(self.master, width=200, height=200)
        self.canvas.create_image(100, 100, image=self.logo_img)
        self.canvas.grid(row=0, column=1)

        self.website_entry = self.create_entry("Website:", 1)
        self.username_entry = self.create_entry("Email/Username:", 2, colspan=2)
        self.password_entry = self.create_entry("Password:", 3)

        self.search_button = self.create_button(text="Search", command=self.search_password, row=1, col=2)
        self.generate_button = self.create_button(text="Generate Password", command=self.generate_password, row=3, col=2)
        self.add_button = self.create_button(text="Add", command=self.save_password, row=4, col=1, colspan=2)

    def create_entry(self, label_text, row, colspan=1):
        tk.Label(self.master, text=label_text).grid(row=row, column=0)
        entry = tk.Entry(self.master)
        entry.grid(row=row, column=1, columnspan=colspan, sticky="EW")
        return entry

    def create_button(self, text, command, row, col, colspan=1):
        button = tk.Button(text=text, command=command)
        button.grid(row=row, column=col, sticky="EW", columnspan=colspan)
        return button

    def generate_password(self):
        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(chars) for _ in range(self.PASSWORD_LENGTH))
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)

    def open_passwords_file(self, filepath="passwords.json"):
        try:
            with open(filepath, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_passwords_file(self, passwords, filepath="passwords.json"):
        with open(filepath, "w") as file:
            json.dump(passwords, file, indent=4)

    def search_password(self):
        website = self.website_entry.get()
        if not website:
            messagebox.showwarning("Warning", "Please enter a website.")
            return
        passwords = self.open_passwords_file()
        if website in passwords:
            username = passwords[website]["username"]
            password = passwords[website]["password"]
            messagebox.showinfo("Info", f"Username: {username}\nPassword: {password}")
        else:
            messagebox.showwarning("Warning", f"No details found for {website}.")

    def save_password(self):
        website = self.website_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        if not all([website, username, password]):
            messagebox.showwarning("Warning", "Please fill out all fields.")
            return
        confirm = messagebox.askokcancel(title="Confirm", message=f"Save details for {website}?")
        if confirm:
            passwords = self.open_passwords_file()
            passwords[website] = {"username": username, "password": password}
            self.save_passwords_file(passwords)

            self.website_entry.delete(0, tk.END)
            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)

            messagebox.showinfo("Info", "Password saved successfully.")

def main():
    root = tk.Tk()
    PasswordManager(root)
    root.mainloop()

if __name__ == "__main__":
    main()