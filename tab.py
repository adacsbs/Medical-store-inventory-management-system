import tkinter as tk
from tkinter import ttk

class TabbedApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Tabbed Application")
        self.geometry("400x300")

        # Create a frame to hold the tab control
        self.tab_frame = tk.Frame(self)
        self.tab_frame.pack(side=tk.LEFT, fill=tk.Y)

        # Create the tab control
        self.tab_control = ttk.Notebook(self.tab_frame)
        self.tab_control.pack(fill=tk.BOTH, expand=True)

        # Create tabs
        self.tab1 = tk.Frame(self.tab_control)
        self.tab2 = tk.Frame(self.tab_control)

        self.tab_control.add(self.tab1, text="Tab 1")
        self.tab_control.add(self.tab2, text="Tab 2")

        # Add content to Tab 1
        self.label1 = tk.Label(self.tab1, text="Content of Tab 1")
        self.label1.pack(pady=20)

        # Add content to Tab 2
        self.label2 = tk.Label(self.tab2, text="Content of Tab 2")
        self.label2.pack(pady=20)

        # Set a trace on tab selection change
        self.tab_control.bind("<<NotebookTabChanged>>", self.on_tab_change)

    def on_tab_change(self, event):
        # Get the current selected tab
        selected_tab = self.tab_control.select()

        # Update the content based on the selected tab
        if selected_tab == self.tab1:
            self.label1.config(text="Content of Tab 1 (Updated)")
        elif selected_tab == self.tab2:
            self.label2.config(text="Content of Tab 2 (Updated)")

# Create an instance of the application
app = TabbedApplication()

# Start the main event loop
app.mainloop()
