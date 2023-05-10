
import tkinter as tk
from tkinter import ttk
import csv

def load_data(tree):
    tree.delete(*tree.get_children())  # Clear the treeview
    with open("data.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            tree.insert("", "end", values=(row["Wrong Number"], row["Grade"]))

def add_data(tree):
    wrong_number = input("Enter Wrong Number: ")
    grade = input("Enter Grade: ")
    tree.insert("", "end", values=(wrong_number, grade))

def remove_data(tree):
    selected_item = tree.selection()[0]
    tree.delete(selected_item)

def edit_data(tree):
    selected_item = tree.selection()[0]
    wrong_number, grade = tree.item(selected_item, "values")

    new_wrong_number = input(f"Enter new Wrong Number (current: {wrong_number}): ")
    new_grade = input(f"Enter new Grade (current: {grade}): ")

    tree.item(selected_item, values=(new_wrong_number, new_grade))

def save_data(tree):
    with open("data.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Wrong Number", "Grade"])

        for row in tree.get_children():
            wrong_number, grade = tree.item(row, "values")
            writer.writerow([wrong_number, grade])

def reset_data(tree):
    load_data(tree)

def main():
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

    remove_button = tk.Button(button_frame, text="Remove", command=lambda: remove_data(tree))
    remove_button.pack(side="left", padx=5)

    edit_button = tk.Button(button_frame, text="Edit", command=lambda: edit_data(tree))
    edit_button.pack(side="left", padx=5)

    save_button = tk.Button(button_frame, text="Save", command=lambda: save_data(tree))
    save_button.pack(side="left", padx=5)

    reset_button = tk.Button(button_frame, text="Reset", command=lambda: reset_data(tree))
    reset_button.pack(side="left", padx=5)

    root.mainloop()

if __name__ == "__main__":
    main()


##issues: buttons not working