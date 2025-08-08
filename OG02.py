import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar

# Add a tax-related deadline
def add_task():
    task = task_entry.get()
    client = client_combo.get()
    date = calendar.get_date()

    if task and client:
        task_listBox.insert(tk.END, f"{task} [Client: {client}] ({date})")
        task_entry.delete(0, tk.END)

# Delete selected deadline
def delete_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        task_listBox.delete(selected_task)

# Mark deadline as completed
def mark_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        task_listBox.itemconfig(selected_task, bg="aquamarine")

# GUI
root = tk.Tk()
root.title("Tax Deadlines Manager")
root.configure(background="bisque")

# Task input
text1 = tk.Label(root, text="Enter Tax Task", bg="bisque")
text1.pack(pady=5)

# Client (Mandant) selection
clients = ["Client A", "Client B", "Client C", "Misc"]
client_label = tk.Label(root, text="Select Client", bg="bisque")
client_label.pack(pady=5)
client_combo = ttk.Combobox(root, values=clients)
client_combo.pack(pady=5)

# Calendar widget (English only)
calendar_label = tk.Label(root, text="Select Date", bg="bisque")
calendar_label.pack(pady=5)
calendar = Calendar(root, selectmode="day", date_pattern="dd.mm.yyyy", locale='en_US')
calendar.pack(pady=10)

# Task entry field
task_entry = tk.Entry(root, width=30, bg="bisque3", fg="brown")
task_entry.pack(pady=10)

# Buttons
add_task_button = tk.Button(root, text="Add Deadline", command=add_task)
add_task_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Deadline", command=delete_task)
delete_button.pack(pady=5)

mark_button = tk.Button(root, text="Mark as Completed", command=mark_task)
mark_button.pack(pady=5)

# Task list
text2 = tk.Label(root, text="Deadlines List", bg="bisque")
text2.pack(pady=5)

task_listBox = tk.Listbox(root, height=10, width=50, bg="azure4")
task_listBox.pack(pady=10)

root.mainloop()