



import tkinter as tk
from tkinter import ttk

def log_action(role, action):
    log_file = f"{role}.log"
    with open(log_file, "a") as f:
        f.write(f"{action}\n")

def log_example(role):
    log_action(role, "Example action performed")

def main():
    root = tk.Tk()
    root.title("Treeview Example")

    tree = ttk.Treeview(root)
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

    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    admin_button = tk.Button(button_frame, text="Log as Admin", command=lambda: log_example("admin"))
    admin_button.pack(side="left", padx=5)

    user_button = tk.Button(button_frame, text="Log as User", command=lambda: log_example("user"))
    user_button.pack(side="left", padx=5)

    root.mainloop()

if __name__ == "__main__":
    main()


##issues: working , but email and pw required