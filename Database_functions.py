import tkinter as tk
from tkinter import ttk
import sqlite3

# Connect to SQLite database (create one if it doesn't exist)
conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# Create a table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS sample_table (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
''')

# Insert some sample data
cursor.execute("INSERT INTO sample_table (name, age) VALUES (?, ?)", ("John Doe", 30))
cursor.execute("INSERT INTO sample_table (name, age) VALUES (?, ?)", ("Jane Smith", 25))
conn.commit()

# Function to fetch data from the SQLite table
def fetch_data():
    cursor.execute("SELECT * FROM sample_table")
    rows = cursor.fetchall()
    return rows

# Function to update the data in the SQLite table
def update_data():
    for row_id in tree.get_children():
        values = [tree.set(row_id, column) for column in tree["columns"]]
        id_value = int(values[0])
        cursor.execute("UPDATE sample_table SET name=?, age=? WHERE id=?", (values[1], values[2], id_value))
    conn.commit()

# Function to handle double-click on a cell
def on_cell_double_click(event):
    item = tree.selection()[0]
    column = tree.identify_column(event.x)
    column = column.split('#')[-1]
    
    # Check if the clicked column is editable
    if column in ["1", "2"]:
        # Create an Entry widget for editing
        entry_widget = tk.Entry(tree, justify="center")
        entry_widget.insert(0, tree.set(item, column))
        entry_widget.grid(row=0, column=int(column)-1, sticky="nsew", padx=1, pady=1)
        
        # Bind the Entry widget to save changes on focus out
        entry_widget.bind("<FocusOut>", lambda e: save_edit(item, column, entry_widget))
        entry_widget.focus_set()

# Function to save edited data back to the Treeview
def save_edit(item, column, entry_widget):
    new_value = entry_widget.get()
    tree.set(item, column, new_value)
    entry_widget.destroy()

# Create the main window
window = tk.Tk()
window.title("SQLite Table Editor")

# Create Treeview widget to display the table
tree = ttk.Treeview(window, columns=("ID", "Name", "Age"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")

# Populate Treeview with data from the SQLite table
data = fetch_data()
for row in data:
    tree.insert("", "end", values=row)

# Add Treeview to the window
tree.pack(padx=10, pady=10)

# Allow double-clicking on a cell to edit the data
tree.bind("<Double-1>", on_cell_double_click)

# Create a button to update the data
update_button = tk.Button(window, text="Update Data", command=update_data)
update_button.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()

# Close the database connection when the window is closed
conn.close()
