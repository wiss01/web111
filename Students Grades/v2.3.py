##updates: login for the user and login for the admin + type



import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Example email, password, and user type pairs
users = {
    "admin@example.com": {"password": "admin_password", "user_type": "admin"},
    "user1@example.com": {"password": "password1", "user_type": "user"},
    "user2@example.com": {"password": "password2", "user_type": "user"},
}

def authenticate(email, password, user_type):
    if email in users and users[email]["password"] == password and users[email]["user_type"] == user_type:
        return True
    return False

def login(login_window, email_var, password_var, user_type_var):
    email = email_var.get()
    password = password_var.get()
    user_type = user_type_var.get()

    if authenticate(email, password, user_type):
        messagebox.showinfo("Login", f"{user_type.capitalize()} Login successful")
        login_window.destroy()
        show_treeview_window()
    else:
        messagebox.showerror("Login", "Invalid email, password or user type")

def show_login_window():
    login_window = tk.Toplevel()
    login_window.title("Login")

    email_var = tk.StringVar()
    password_var = tk.StringVar()
    user_type_var = tk.StringVar()

    email_label = tk.Label(login_window, text="Email:")
    email_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    email_entry = tk.Entry(login_window, textvariable=email_var)
    email_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    password_label = tk.Label(login_window, text="Password:")
    password_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
    password_entry = tk.Entry(login_window, textvariable=password_var, show="*")
    password_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    user_type_label = tk.Label(login_window, text="User Type:")
    user_type_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
    user_type_combobox = ttk.Combobox(login_window, textvariable=user_type_var, values=("admin", "user"))
    user_type_combobox.grid(row=2, column=1, padx=5, pady=5, sticky="w")
    user_type_combobox.current(0)

    login_button = tk.Button(login_window, text="Login", command=lambda: login(login_window, email_var, password_var, user_type_var))
    login_button.grid(row=3, column=1, padx=5, pady=5, sticky="e")

# The rest of the code (show_treeview_window, main function) remains the same as in the previous example


def main():
    root = tk.Tk()
    root.title("Login Example")

    login_button = tk.Button(root, text="Login", command=show_login_window)
    login_button.pack(padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
    
    
    
##issues: working, but add to this login , the tree