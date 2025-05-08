import tkinter as tk
from tkinter import messagebox
import math  # Needed for square root

# Function Definitions
def add():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result_var.set(f"Result: {num1 + num2}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")

def subtract():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result_var.set(f"Result: {num1 - num2}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")

def multiply():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result_var.set(f"Result: {num1 * num2}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")

def divide():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if num2 == 0:
            raise ZeroDivisionError
        result_var.set(f"Result: {num1 / num2}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")
    except ZeroDivisionError:
        messagebox.showerror("Math error", "Cannot divide by zero.")

def square():
    try:
        num = float(entry1.get())
        result_var.set(f"Result: {num ** 2}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number in the first input.")

def square_root():
    try:
        num = float(entry1.get())
        if num < 0:
            raise ValueError("Cannot take square root of negative number.")
        result_var.set(f"Result: {math.sqrt(num)}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a non-negative number in the first input.")

# GUI Setup
root = tk.Tk()
root.title("Simple Calculator")

# Widgets
tk.Label(root, text="Enter first number:").grid(row=0, column=0, padx=10, pady=5)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, pady=5)

tk.Label(root, text="Enter second number:").grid(row=1, column=0, padx=10, pady=5)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, pady=5)

# Buttons for operations
tk.Button(root, text="Add", width=10, command=add).grid(row=2, column=0, pady=5)
tk.Button(root, text="Subtract", width=10, command=subtract).grid(row=2, column=1, pady=5)
tk.Button(root, text="Multiply", width=10, command=multiply).grid(row=3, column=0, pady=5)
tk.Button(root, text="Divide", width=10, command=divide).grid(row=3, column=1, pady=5)

# Buttons for square and square root operations
tk.Button(root, text="Square", width=10, command=square).grid(row=4, column=0, pady=5)
tk.Button(root, text="√ Square Root", width=15, command=square_root).grid(row=4, column=1, pady=5)

# Result label
result_var = tk.StringVar()
tk.Label(root, textvariable=result_var, font=("Arial", 14), fg="blue").grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()


result_var = tk.StringVar()
result_var.set("Result:")
tk.Label(root, textvariable=result_var, font=("Arial", 12)).grid(row=4, columnspan=2, pady=10)

# Run the application
root.mainloop()
