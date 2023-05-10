##updates:providing login to the tree


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

def login(login_window, email_var, password_var):
    email = email_var.get()
    password = password_var.get()

    if authenticate(email, password):
        messagebox.showinfo("Login", "Login successful")
        login_window.destroy()
        show_treeview_window()
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

def show_treeview_window():
    tree_window = tk.Toplevel()
    tree_window.title("Treeview Example")

    tree = ttk.Treeview(tree_window)
    tree.pack(expand=True, fill="both")

    root_node = tree.insert("", "end", text="Root Node", open=True)

    node1 = tree.insert(root_node, "end", text="Node 1: License", open=True)
    sub_node1 = tree.insert(node1, "end", text="Sub-node 1: LCS", open=True)
    tree.insert(sub_node1, "end", text="-1 LCS")
    tree.insert(sub_node1, "end", text="-2 LCS:")
    tree.insert(sub_node1, "end", text="  -GLSI")
    tree.insert(sub_node1, "end", text="  -MI")
    tree.insert(sub_node1, "end", text="-3 LCS:")
    tree.insert(sub_node1, "end", text="  -GLSI")
    tree.insert(sub_node1, "end", text="  -MI")
    tree.insert(node1, "end", text="Sub-node 2: LCE")
    tree.insert(node1, "end", text="Sub-node 2: LBC")

    node2 = tree.insert(root_node, "end", text="Node 2: Master", open=True)
    tree.insert(node2, "end", text="Sub-node 3:")
    tree.insert(node2, "end", text="Sub-node 4:")

def main():
    root = tk.Tk()
    root.title("Login Example")

    login_button = tk.Button(root, text="Login", command=show_login_window)
    login_button.pack(padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()


##issues: we should have a login for the admin and an other for the user 