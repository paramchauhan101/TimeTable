import tkinter as tk
from tkinter import messagebox, ttk
import json
import os

# File to store the data
DATA_FILE = "reminders_notes.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Function to add reminder and note
def add_reminder_note():
    reminder = reminder_entry.get()
    note = note_entry.get()
    
    if not reminder or not note:
        messagebox.showwarning("Input Error", "Please enter both reminder and note.")
        return
    
    data = load_data()
    data.append({"reminder": reminder, "note": note})
    save_data(data)
    
    display_area.config(state=tk.NORMAL)
    display_area.insert(tk.END, f"Reminder: {reminder}\nNote: {note}\n\n")
    display_area.config(state=tk.DISABLED)
    
    reminder_entry.delete(0, tk.END)
    note_entry.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Reminder and Note App")
root.geometry("600x400")
root.configure(bg="#f0f0f0")

# Styling
style = ttk.Style()
style.configure("TButton",
                background="#007bff",
                foreground="#ffffff",
                padding=10,
                font=("Arial", 12, "bold"))
style.configure("TLabel",
                background="#f0f0f0",
                font=("Arial", 12))
style.configure("TEntry",
                font=("Arial", 12))

# Create and place widgets
header = tk.Label(root, text="Reminder and Note App", font=("Arial", 18, "bold"), bg="#f0f0f0", pady=10)
header.pack()

form_frame = tk.Frame(root, bg="#f0f0f0")
form_frame.pack(pady=10)

tk.Label(form_frame, text="Reminder:", bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=5, sticky="w")
reminder_entry = ttk.Entry(form_frame, width=50)
reminder_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(form_frame, text="Note:", bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=5, sticky="w")
note_entry = ttk.Entry(form_frame, width=50)
note_entry.grid(row=1, column=1, padx=10, pady=5)

add_button = ttk.Button(root, text="Add Reminder and Note", command=add_reminder_note)
add_button.pack(pady=10)

display_area = tk.Text(root, height=10, width=70, state=tk.DISABLED, wrap=tk.WORD, bg="#ffffff", font=("Arial", 12))
display_area.pack(pady=10)

# Load existing data and display it
def load_and_display_data():
    data = load_data()
    display_area.config(state=tk.NORMAL)
    for item in data:
        display_area.insert(tk.END, f"Reminder: {item['reminder']}\nNote: {item['note']}\n\n")
    display_area.config(state=tk.DISABLED)

load_and_display_data()

# Start the main event loop
root.mainloop()
