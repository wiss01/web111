##updates:trying to integrate this app with Flask app web



import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import csv

def load_users_from_csv(filename="users.csv"):
    users = {}
    with open(filename, mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            email = row['email']
            user_data = {k: row[k] for k in ('password', 'user_type', 'allowed_path')}
            users[email] = user_data
    return users

users = load_users_from_csv()

def save_users_to_csv(users, filename="users.csv"):
    fieldnames = ['email', 'password', 'user_type', 'allowed_path']
    with open(filename, mode='w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for email, user_data in users.items():
            row = {'email': email, **user_data}
            writer.writerow(row)

def set_allowed_path(tree, email_var):
    email = email_var.get()
    
    if email in users:
        item = tree.selection()[0]
        users[email]["allowed_path"] = tree.item(item, "text")
        messagebox.showinfo("Admin", f"Allowed path for {email} set to {users[email]['allowed_path']}")
        save_users_to_csv(users)
    else:
        messagebox.showerror("Admin", "Invalid user email")

def open_admin_window(tree):
    admin_window = tk.Toplevel()
    admin_window.title("Admin: Set Allowed Path")

    email_var = tk.StringVar()
    email_label = tk.Label(admin_window, text="User Email:")
    email_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    email_entry = tk.Entry(admin_window, textvariable=email_var)
    email_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    set_path_button = tk.Button(admin_window, text="Set Allowed Path", command=lambda: set_allowed_path(tree, email_var))
    set_path_button.grid(row=1, column=1, padx=5, pady=5, sticky="e")



def build_tree(tree, tree_structure, parent):
    for item in tree_structure:
        node_text, children = item
        node = tree.insert(parent, "end", text=node_text, open=True)
        build_tree(tree, children, node)













def show_treeview_window(user_type, email):
    treeview_window = tk.Toplevel()
    treeview_window.title("Treeview Example")

    tree = ttk.Treeview(treeview_window)
    tree.pack(expand=True, fill="both")

    root_node = tree.insert("", "end", text="Root Node", open=True)

    # Define your tree structure here
    tree_structure = [
        ("Node 1: License", [
            ("Sub-node 1: LCS", [("Sub-node 1: SysR", [])]),
            ("Sub-node 2: LCE", []),
            ("Sub-node 3: LBC", []),
        ]),
        ("Node 2: Master", [
            ("Sub-node 3:", []),
            ("Sub-node 4:", []),
        ]),
    ]

    build_tree(tree, tree_structure, root_node)

    # Add double-click binding

    
    
    tree.bind("<Double-1>", lambda event, tree=tree, treeview_window=treeview_window: on_tree_double_click(event, tree, treeview_window))




    if user_type == "user":
        allowed_path = users[email]["allowed_path"]

        def find_subtree(tree_structure, allowed_path):
            for item in tree_structure:
                node_text, children = item
                if node_text == allowed_path:
                    return [item]
                subtree = find_subtree(children, allowed_path)
                if subtree:
                    return subtree
            return None

        allowed_subtree = find_subtree(tree_structure, allowed_path)

        if allowed_subtree:
            tree.pack_forget()  # Hide the original tree

            new_tree = ttk.Treeview(treeview_window)
            new_tree.pack(expand=True, fill="both")
            build_tree(new_tree, allowed_subtree, "")

    if user_type == "admin":
        open_admin_button = tk.Button(treeview_window, text="Open Admin Window", command=lambda: open_admin_window(tree))
        open_admin_button.pack(padx=5, pady=5)

    ##treeview_window.mainloop()

 
def main_buttons():
    ##if parent is None:
    ##    root = tk.Tk()
    ##    root.title("Login Example")
    ##else:
        ##root = parent
        ##root.title("Management Buttons")
       ## root.mainloop()
    
        def load_data(tree):
            tree.delete(*tree.get_children())  # Clear the treeview
            with open("data.csv", "r") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    tree.insert("", "end", values=(row["Wrong Number"], row["Grade"]))
        
        def add_data(tree):
            # Create a new window for adding data
            add_window = tk.Toplevel()
            add_window.title("Add Data")
        
            # Create entry fields for wrong number and grade
            wrong_number_label = tk.Label(add_window, text="Wrong Number:")
            wrong_number_label.pack()
            wrong_number_entry = tk.Entry(add_window)
            wrong_number_entry.pack()
        
            grade_label = tk.Label(add_window, text="Grade:")
            grade_label.pack()
            grade_entry = tk.Entry(add_window)
            grade_entry.pack()
        
            # Add button to save new data and close the window
            save_button = tk.Button(add_window, text="Save", command=lambda: save_new_data(tree, add_window, wrong_number_entry.get(), grade_entry.get()))
            save_button.pack()
                                                                            
        
        ##    add_window.destroy()
        
        def remove_data(tree):
            selected_item = tree.selection()[0]
            tree.delete(selected_item)
        
        def edit_data(tree):
            selected_item = tree.selection()[0]
            wrong_number, grade = tree.item(selected_item, "values")
        
            # Create a new window for editing data
            edit_window = tk.Toplevel()
            edit_window.title("Edit Data")
        
            # Create entry fields for wrong number and grade
            wrong_number_label = tk.Label(edit_window, text="Wrong Number:")
            wrong_number_label.pack()
            wrong_number_entry = tk.Entry(edit_window)
            wrong_number_entry.insert(0, wrong_number)
            wrong_number_entry.pack()
        
            grade_label = tk.Label(edit_window, text="Grade:")
            grade_label.pack()
            grade_entry = tk.Entry(edit_window)
            grade_entry.insert(0, grade)
            grade_entry.pack()
        
            # Add button to save edited data and close the window
            save_button = tk.Button(edit_window, text="Save", command=lambda: save_edited_data(tree, edit_window, selected_item, wrong_number_entry.get(), grade_entry.get()))
            save_button.pack()
        
        def save_edited_data(tree, edit_window, selected_item, wrong_number, grade):
            # Update the values of the selected item in the treeview and CSV file
            tree.item(selected_item, values=(wrong_number, grade))
            with open("data.csv", "r+") as csvfile:
                reader = csv.DictReader(csvfile)
                rows = list(reader)
                for row in rows:
                    if row["Wrong Number"] == selected_item["values"][0]:
                        row["Wrong Number"] = wrong_number
                        row["Grade"] = grade
                csvfile.seek(0)
                writer = csv.DictWriter(csvfile, fieldnames=["Wrong Number", "Grade"])
                writer.writeheader()
                writer.writerows(rows)
        
            # Close the edit window
            edit_window.destroy()
        
        
        def save_new_data(tree, add_window, wrong_number, grade):
            tree.insert("", "end", values=(wrong_number, grade))
            with open("data.csv", "a", newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([wrong_number, grade])
            add_window.destroy()
   
        
        
        
        
        ##save data to the csv DataBase
        def save_data(tree):
            with open("data.csv", "w", newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["Wrong Number", "Grade"])
        
                for row in tree.get_children():
                    wrong_number, grade = tree.item(row, "values")
                    writer.writerow([wrong_number, grade])
        
        def reset_data(tree):
            load_data(tree)
        
        ##def main():
        root = tk.Tk()
        root.title("Treeview Example")
        # Create a Treeview with two columns: Wrong Number and Grade
        tree = ttk.Treeview(root, columns=("wrong_number", "grade"), show="headings")
        tree.pack(expand=True, fill="both")
        # Set column headings
        tree.heading("wrong_number", text="Wrong Number")
        tree.heading("grade", text="Grade")
        # Set column widths
        tree.column("wrong_number", width=100)
        tree.column("grade", width=100)
        # Load data from CSV file
        load_data(tree)
        # Management buttons
        button_frame = tk.Frame(root)
        button_frame.pack(fill="x", padx=5, pady=5)
        add_button = tk.Button(button_frame, text="Add", command=lambda: add_data(tree))
        add_button.pack(side="left", padx=5)
        remove_button = tk.Button(button_frame,text="Remove", command=lambda: remove_data(tree))
        remove_button.pack(side="left", padx=5)
        
        edit_button = tk.Button(button_frame, text="Edit", command=lambda: edit_data(tree))
        edit_button.pack(side="left", padx=5)
        
        
        reset_button = tk.Button(button_frame, text="Reset", command=lambda: reset_data(tree))
        reset_button.pack(side="left", padx=5)
                    
            ##root.mainloop()






def open_management_window():
    ##management_window = tk.Toplevel()
    ##management_window.title("Management Window")
    main_buttons()

    

def on_tree_double_click(event, tree, treeview_window):
    item_id = tree.selection()[0]
    item = tree.item(item_id)
    node_text = item["text"]

    if node_text == "Sub-node 1: SysR":
        open_management_window()

 
 
    
    
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
        messagebox.showerror("Login", "Invalid email, password, or user type")









def main():
    root1 = tk.Tk()
    root1.title("Login2 Example")
    
    login_button = tk.Button(root1, text="Login", command=lambda: show_login_window())
    login_button.pack(padx=5, pady=5)
    
    root1.mainloop()
    
    
if __name__ == "__main__":
    main()



##issues: none  