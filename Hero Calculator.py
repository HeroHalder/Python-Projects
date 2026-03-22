import tkinter as tk

# Function to update expression
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

# Function to evaluate expression
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set("Error")
        expression = ""

# Function to clear
def clear():
    global expression
    expression = ""
    equation.set("")

# GUI Setup
root = tk.Tk()
root.title("Hero Calculator 🧮")
root.geometry("300x400")
root.configure(bg="black")

expression = ""
equation = tk.StringVar()

# Display
entry = tk.Entry(
    root,
    textvariable=equation,
    font=('Arial', 20),
    bg="black",
    fg="white",
    bd=5,
    relief="flat",
    justify="right"
)
entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

# Button style (bg removed to avoid conflict)
btn_style = {
    "font": ("Arial", 14),
    "fg": "white",
    "bd": 0,
    "width": 5,
    "height": 2
}

# Buttons Frame
frame = tk.Frame(root, bg="black")
frame.pack()

# Buttons Layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', 'C', '=', '+']
]

# Create Buttons
for row in buttons:
    row_frame = tk.Frame(frame, bg="black")
    row_frame.pack()

    for btn in row:
        if btn == "=":
            tk.Button(
                row_frame, text=btn, **btn_style,
                bg="#00aa00", command=equalpress
            ).pack(side="left", padx=5, pady=5)

        elif btn == "C":
            tk.Button(
                row_frame, text=btn, **btn_style,
                bg="#aa0000", command=clear
            ).pack(side="left", padx=5, pady=5)

        else:
            tk.Button(
                row_frame, text=btn, **btn_style,
                bg="#333", command=lambda b=btn: press(b)
            ).pack(side="left", padx=5, pady=5)

# Run app
root.mainloop()
