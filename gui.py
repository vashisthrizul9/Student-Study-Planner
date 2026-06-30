from tkinter import messagebox
from datetime import datetime
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Student Study Planner")
app.geometry("900x700")
app.title("Student Study Planner Pro")
app.resizable(False, False)

title = ctk.CTkLabel(
    app,
    text="Student Study Planner",
    font=("Arial", 28, "bold")
)
title.pack(pady=20)
today = datetime.now().strftime("%d/%m/%Y")

date_label = ctk.CTkLabel(
    app,
    text=f"Date: {today}",
    font=("Arial", 16)
)
date_label.pack(pady=5)

name_label = ctk.CTkLabel(app, text="Student Name")
name_label.pack()

name_entry = ctk.CTkEntry(app, width=300)
name_entry.pack(pady=10)
subject1_label = ctk.CTkLabel(app, text="Subject 1")
subject1_label.pack()

subject1_entry = ctk.CTkEntry(app, width=300)
subject1_entry.pack(pady=5)

subject2_label = ctk.CTkLabel(app, text="Subject 2")
subject2_label.pack()

subject2_entry = ctk.CTkEntry(app, width=300)
subject2_entry.pack(pady=5)

subject3_label = ctk.CTkLabel(app, text="Subject 3")
subject3_label.pack()

subject3_entry = ctk.CTkEntry(app, width=300)
subject3_entry.pack(pady=5)
hours_label = ctk.CTkLabel(app, text="Total Study Hours")
hours_label.pack()

hours_entry = ctk.CTkEntry(app, width=300)
hours_entry.pack(pady=5)
progress = ctk.CTkProgressBar(app, width=300)
progress.pack(pady=10)
progress.set(0)

def generate():
    student = name_entry.get().strip()
    subject1 = subject1_entry.get().strip()
    subject2 = subject2_entry.get().strip()
    subject3 = subject3_entry.get().strip()
    hours_text = hours_entry.get().strip()

    if not student:
        messagebox.showerror("Error", "Please enter your name.")
        return

    if not subject1 or not subject2 or not subject3:
        messagebox.showerror("Error", "Please enter all subjects.")
        return

    if not hours_text:
        messagebox.showerror("Error", "Please enter total study hours.")
        return

    try:
        hours = float(hours_text)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for study hours.")
        return

    if hours <= 0:
        messagebox.showerror("Error", "Study hours must be greater than 0.")
        return

    each = round(hours / 3, 1)

    result.configure(
        text=f"""
Student : {student}

📚 Study Plan

{subject1} : {each} Hours
{subject2} : {each} Hours
{subject3} : {each} Hours

Total Study Time : {hours} Hours

Good Luck!
"""
    )
    progress.set(1)

button = ctk.CTkButton(
    app,
    text="Generate Plan",
    command=generate
)
button.pack(pady=20)

result = ctk.CTkLabel(app, text="")
result.pack()

def save_plan():
    with open("study_plan.txt", "w") as file:
        file.write(result.cget("text"))

    messagebox.showinfo("Success", "Study Plan Saved!")

save_button = ctk.CTkButton(
    app,
    text="Save Plan",
    command=save_plan
)
save_button.pack(pady=10)
def reset():
    name_entry.delete(0, "end")
    subject1_entry.delete(0, "end")
    subject2_entry.delete(0, "end")
    subject3_entry.delete(0, "end")
    hours_entry.delete(0, "end")

    result.configure(text="")
    progress.set(0)

reset_button = ctk.CTkButton(
    app,
    text="Reset",
    command=reset,
    fg_color="red"
)
reset_button.pack(pady=10)

app.mainloop()

