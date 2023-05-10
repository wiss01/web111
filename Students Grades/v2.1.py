##updates: the mail and pw provided 


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Example email and password pairs
users = {
    "user1@example.com": "password1",
    "user2@example.com": "password2",
}

def authenticate(email, password):
    if email in users and users[email] == password:
        return True
    return False

def login(root, email_var, password_var):
    email = email_var.get()
    password = password_var.get()

    if authenticate(email, password):
        messagebox.showinfo("Login", "Login successful")
        root.destroy()
    else:
        messagebox.showerror("Login", "Invalid email or password")

def show_login_window():
    login_window = tk.Toplevel()
    login_window.title("Login")

    email_var = tk.StringVar()
    password_var = tk.StringVar()

    email_label = tk.Label(login_window, text="Email:")
    email_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    email_entry = tk.Entry(login_window, textvariable=email_var)
    email_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    password_label = tk.Label(login_window, text="Password:")
    password_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
    password_entry = tk.Entry(login_window, textvariable=password_var, show="*")
    password_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    login_button = tk.Button(login_window, text="Login", command=lambda: login(login_window, email_var, password_var))
    login_button.grid(row=2, column=1, padx=5, pady=5, sticky="e")

def main():
    root = tk.Tk()
    root.title("Treeview Example")

    login_button = tk.Button(root, text="Login", command=show_login_window)
    login_button.pack(padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()


##issues: working ,but should combined with the tree