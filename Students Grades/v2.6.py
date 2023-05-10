##updates:allowed path is identified 
# by the admin not by the Programmer 

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Add allowed_path to the users dictionary
users = {
    "admin@example.com": {"password": "admin_password", "user_type": "admin", "allowed_path": ""},
    "user1@example.com": {"password": "password1", "user_type": "user", "allowed_path": ""},
    "user2@example.com": {"password": "password2", "user_type": "user", "allowed_path": ""},
}





def set_allowed_path(tree, email_var):
    email = email_var.get()
    
    if email in users and users[email]["user_type"] == "user":
        item = tree.selection()[0]
        users[email]["allowed_path"] = tree.item(item, "text")
        messagebox.showinfo("Admin", f"Allowed path for {email} set to {users[email]['allowed_path']}")
    else:
        messagebox.showerror("Admin", "Invalid user email or user is an admin")




# Add this function to open the admin window for setting allowed paths
def open_admin_window():
    admin_window = tk.Toplevel()
    admin_window.title("Admin: Set Allowed Path")

    global email_set


    email_set = tk.StringVar()
    email_label = tk.Label(admin_window, text="User Email:")
    email_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    email_entry_set = tk.Entry(admin_window, textvariable=email_set)
    email_entry_set.grid(row=0, column=1, padx=5, pady=5, sticky="w")


    set_path_button = tk.Button(admin_window, text="Set Allowed Path", command=lambda:set_allowed_path(tree, email_entry_set))
    set_path_button.grid(row=1, column=1, padx=5, pady=5, sticky="e")



def set_allowed_path(tree, email_entry_set):
    
    global email_set
    email_set = email_entry_set.get()   
    
    
    if email_set in users and users[email]["user_type"] == "user":
        item = tree.selection()[0]
        users[email]["allowed_path"] = tree.item(item, "text")
        messagebox.showinfo("Admin", f"Allowed path for {email} set to {users[email]['allowed_path']}")
    else:
        messagebox.showerror("Admin", "Invalid user email or user is an admin")




def show_treeview_window(user_type, allowed_path):
    treeview_window = tk.Toplevel()
    treeview_window.title("Treeview Example")

    tree = ttk.Treeview(treeview_window)
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
    
    
    if user_type == "user":
        for item in tree.get_children():
            if tree.item(item, "text") != allowed_path:
                tree.detach(item)

    treeview_window.mainloop()






def set_allowed_path():
    
        email_var = tk.StringVar()
        email = email_var.get()
        if email in users and users[email]["user_type"] == "user":
            item = tree.selection()[0]
            users[email]["allowed_path"] = tree.item(item, "text")
            messagebox.showinfo("Admin", f"Allowed path for {email} set to {users[email]['allowed_path']}")
        else:
            messagebox.showerror("Admin", "Invalid user email or user is an admin")
        login_window = tk.Toplevel()
        









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
        show_treeview_window(user_type, email)
    else:
        messagebox.showerror("Login", "Invalid email, password or user type")
        
        
def main():

    ##root = tk.Tk()
    ##
    ##root.title("Login Example")
    
    
    
    root = tk.Tk()    
        
    login_button = tk.Button(root, text="Login1", command=lambda:show_login_window())
    login_button.pack(padx=5, pady=5)
    
    admin_button = tk.Button(root, text="Admin: Set Allowed Path", command=lambda:open_admin_window())
    admin_button.pack(padx=5, pady=5)
    
    root.mainloop()



if __name__ == "__main__":
    main()



##issues: admin can't access the treeview afterinput the user email
## to id the allowed path