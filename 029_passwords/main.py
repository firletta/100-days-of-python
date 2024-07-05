import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordManager:
    PASSWORD_LENGTH = 12
    ENTRY_WIDTH = 35
    BUTTON_WIDTH = 36
    PADX = 40
    PADY = 40

    def __init__(self, master):
        self.master = master
        self.master.title("Password Manager")
        self.master.config(padx=self.PADX, pady=self.PADY)
        self.setup_ui()

    def setup_ui(self):
        # Logo
        self.logo_img = tk.PhotoImage(file="logo.png")
        self.canvas = tk.Canvas(self.master, width=200, height=200)
        self.canvas.create_image(100, 100, image=self.logo_img)
        self.canvas.grid(row=0, column=1)

        # Entries and Labels
        self.website_entry = self.create_entry("Website:", 1)
        self.username_entry = self.create_entry("Email/Username:", 2)
        self.password_entry = self.create_entry("Password:", 3, self.PASSWORD_LENGTH)

        # Buttons
        self.add_button = tk.Button(text="Add", width=self.BUTTON_WIDTH, command=self.save_password)
        self.add_button.grid(row=4, column=1, columnspan=2)

        self.generate_button = tk.Button(text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=3, column=2, sticky="EW")

    def create_entry(self, label_text, row, width=None):
        tk.Label(self.master, text=label_text).grid(row=row, column=0)
        entry = tk.Entry(self.master, width=width or self.ENTRY_WIDTH)
        entry.grid(row=row, column=1, columnspan=2, sticky="EW")
        return entry

    def generate_password(self, event=None):
        password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(self.PASSWORD_LENGTH))
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)

    def save_password(self):
        website = self.website_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        if not all([website, username, password]):
            messagebox.showwarning("Warning", "Please fill out all fields.")
            return
        confirm = messagebox.askokcancel(title="Confirm", message=f"Save details for {website}?")
        if confirm:
            with open("passwords.txt", "a") as file:
                file.write(f"{website} | {username} | {password}\n")
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