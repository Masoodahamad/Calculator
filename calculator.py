import tkinter as tk

# Function to perform arithmetic operations
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(current) + str(number))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create main window
window = tk.Tk()
window.title("Calculator")

# Create entry field
entry = tk.Entry(window, font=('Arial', 20), bd=5, justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define button labels
button_labels = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Create buttons
buttons = []
for i, label in enumerate(button_labels):
    row = i // 4 + 1
    col = i % 4
    if label == 'C':
        button = tk.Button(window, text=label, font=('Arial', 15), padx=20, pady=20, command=clear)
    elif label == '=':
        button = tk.Button(window, text=label, font=('Arial', 15), padx=20, pady=20, command=calculate)
    else:
        button = tk.Button(window, text=label, font=('Arial', 15), padx=20, pady=20, command=lambda num=label: button_click(num))
    button.grid(row=row, column=col, padx=5, pady=5)
    buttons.append(button)

# Run the application
window.mainloop()
