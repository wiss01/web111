import tkinter as tk
from tkinter import ttk

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

    root.mainloop()

if __name__ == "__main__":
    main()
