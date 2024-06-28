import tkinter as tk

def update_text():
    new_text = entry.get()
    print("Updated Text:", new_text)

# Create the main window
window = tk.Tk()
window.title("Text Field Demo")

# Create a label and entry widget
label = tk.Label(window, text="Enter Text:")
label.pack(pady=10)

default_text = "Default Text"
entry = tk.Entry(window, width=30)
entry.insert(0, default_text)  # Set default text
entry.pack(pady=10)

# Create a button to update the text
update_button = tk.Button(window, text="Update Text", command=update_text)
update_button.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()
