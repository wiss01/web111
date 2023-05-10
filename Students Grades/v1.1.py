##updates: management buttons implementations



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

    remove_button = tk.Button(button_frame,text="Remove", command=lambda: remove_data(tree))
    remove_button.pack(side="left", padx=5)
    
    edit_button = tk.Button(button_frame, text="Edit", command=lambda: edit_data(tree))
    edit_button.pack(side="left", padx=5)
    
    
    reset_button = tk.Button(button_frame, text="Reset", command=lambda: reset_data(tree))
    reset_button.pack(side="left", padx=5)
    
    root.mainloop()
    
    
if __name__ == "__main__":
    main()



##issuses: missing search&filter bar