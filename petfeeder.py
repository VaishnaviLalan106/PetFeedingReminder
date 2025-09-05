import tkinter as tk
from tkinter import messagebox, ttk
from ttkthemes import ThemedTk
import datetime
from PIL import Image, ImageTk
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
import os, sys
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS 
    except Exception:
        base_path = os.path.abspath(".") 
    return os.path.join(base_path, relative_path)
img_path = resource_path("paw_transparent.png")
root = ThemedTk(theme="breeze")
root.title("Pet Feeding Reminder 🐾")
root.geometry("450x350")
root.configure(bg="#E6E6FA") 
paw_img = Image.open(img_path)
paw_img = paw_img.resize((60, 60))
paw_photo = ImageTk.PhotoImage(paw_img)
paw_label = tk.Label(root, image=paw_photo, bg="#E6E6FA")
paw_label.image = paw_photo
paw_label.pack(pady=5)
title = tk.Label(root, text="🐶 Pet Feeding Reminder 🐾",font=("Comic Sans MS", 16, "bold"),bg="#E6E6FA", fg="#333")
title.pack(pady=10)
time_label = tk.Label(root, text="Enter time in HH:MM AM/PM format:",font=("Arial", 11), bg="#E6E6FA")
time_label.pack(pady=5)
time_entry = ttk.Entry(root, width=20, font=("Arial", 12))
time_entry.pack(pady=5)
status_label = tk.Label(root, text="", font=("Arial", 11),bg="#E6E6FA", fg="darkblue")
status_label.pack(pady=5)
reminder_time = None 
def set_reminder():
    global reminder_time
    user_input = time_entry.get().strip().upper()
    try:
        datetime.datetime.strptime(user_input, "%I:%M %p")
        reminder_time = user_input
        status_label.config(text=f"⏰ Reminder set for: {reminder_time}")
    except ValueError:
        messagebox.showerror("Invalid Format", "Please enter time in HH:MM AM/PM format.\nExample: 03:45 PM")
def check_reminder():
    global reminder_time
    if reminder_time:
        now = datetime.datetime.now().strftime("%I:%M %p")
        if now == reminder_time:
            messagebox.showinfo("Reminder 🐾", "Time to feed your pet! 🐶💕")
            reminder_time = None  
            status_label.config(text="✅ Reminder completed!")
    root.after(1000, check_reminder) 
set_button = ttk.Button(root, text="Set Reminder 🐾", command=set_reminder)
set_button.pack(pady=10)
footer = tk.Label(root, text="Made with 🐾 for your pets 💖",font=("Comic Sans MS", 10), bg="#E6E6FA", fg="#444")
footer.pack(side="bottom", pady=10)
check_reminder()
root.mainloop()
