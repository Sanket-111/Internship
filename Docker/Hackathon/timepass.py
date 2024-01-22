import tkinter as tk
from tkinter import ttk

iphone_width = 700
iphone_height = 500

def newWindow(firstselection):
    new_window = tk.Toplevel(root)
    new_window.title(f"Machine {firstselection}")
    new_window.geometry(f"{iphone_width}x{iphone_height}")

    if firstselection == "Windows":
        questions = ["Question 1", "Question 2", "Question 3"]
        answers = [1,1,1]
        options1 = ["Yes", "No"]

        

        for question in questions:
            question_label = tk.Label(new_window, text=question)
            question_label.pack(pady=10)

            dropdown = ttk.Combobox(new_window, textvariable=dropdown_var, values=options1)
            dropdown.set(options1[0]) 
            dropdown.pack(pady=10)

            submit_button = tk.Button(root, text="Submit", command=submit_action1)
            submit_button.pack(pady=10)
            

def submit_action1():
    pass

def submit_action():
    global dropdown_var 
    selected_answer = dropdown_var.get()
    firstselection = selected_answer
    newWindow(firstselection)


root = tk.Tk()
root.title("Operating System Selection")
root.geometry(f"{iphone_width}x{iphone_height}")

question_label = tk.Label(root, text="Operating System You Use:")
question_label.pack(pady=10)

dropdown_var = tk.StringVar()

options = ["Windows", "Linux", "Mac OS"]
dropdown = ttk.Combobox(root, textvariable=dropdown_var, values=options)
dropdown.set(options[0]) 
dropdown.pack(pady=10)

submit_button = tk.Button(root, text="Submit", command=submit_action)
submit_button.pack(pady=10)

root.mainloop()
