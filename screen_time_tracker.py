# ======================================================
# PERSONAL SCREEN-TIME & STUDY BALANCE TRACKER
# Class 12 CBSE Project
# Language: Python
# GUI: Tkinter
# Purpose: Track study hours vs screen time ethically
# ======================================================

import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# ------------------------------------------------------
# Function to submit daily data
# ------------------------------------------------------
def submit_data():
    """
    Collects study hours and screen time from user,
    calculates balance, stores it in a local file, 
    and gives feedback if screen time exceeds study time.
    """
    try:
        study_hours = float(study_entry.get())
        screen_hours = float(screen_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")
        return

    # Calculate balance
    balance = study_hours - screen_hours

    # Feedback message
    if balance < 0:
        feedback = "Warning: Screen time exceeds study time!"
    elif balance == 0:
        feedback = "Balance is neutral today."
    else:
        feedback = "Good job! Study time exceeds screen time."

    # Display feedback
    result_label.config(text=f"Balance: {balance} hours\n{feedback}")

    # Save data locally
    with open("tracker.txt", "a") as file:
        file.write(f"Date: {datetime.now().strftime('%Y-%m-%d')}\n")
        file.write(f"Study Hours: {study_hours}\n")
        file.write(f"Screen Hours: {screen_hours}\n")
        file.write(f"Balance: {balance} | {feedback}\n")
        file.write("-"*30 + "\n")

    # Clear input fields
    study_entry.delete(0, tk.END)
    screen_entry.delete(0, tk.END)

# ------------------------------------------------------
# Function to view weekly/monthly summary
# ------------------------------------------------------
def view_summary():
    """
    Opens a new window to display all stored data from tracker.txt
    """
    try:
        with open("tracker.txt", "r") as file:
            content = file.read()
    except FileNotFoundError:
        content = "No data found."

    summary_window = tk.Toplevel(root)
    summary_window.title("Screen-Time Tracker Summary")
    text_area = tk.Text(summary_window, width=60, height=25)
    text_area.pack()
    text_area.insert(tk.END, content)

# ------------------------------------------------------
# GUI Design
# ------------------------------------------------------
root = tk.Tk()
root.title("Screen-Time & Study Balance Tracker")
root.geometry("500x450")

# Heading
tk.Label(root, text="Screen-Time & Study Balance Tracker",
         font=("Arial", 14, "bold")).pack(pady=10)

# Study Hours Input
tk.Label(root, text="Enter Study Hours Today").pack()
study_entry = tk.Entry(root)
study_entry.pack()

# Screen Time Input
tk.Label(root, text="Enter Screen Time Hours Today").pack()
screen_entry = tk.Entry(root)
screen_entry.pack()

# Submit Button
tk.Button(root, text="Submit Data", command=submit_data).pack(pady=10)

# View Summary Button
tk.Button(root, text="View Summary", command=view_summary).pack(pady=5)

# Feedback Label
result_label = tk.Label(root, text="", fg="green", font=("Arial", 12))
result_label.pack(pady=10)

# Footer
tk.Label(root, text="Your data is stored locally and remains private",
         fg="blue").pack(pady=10)

# Run the GUI
root.mainloop()