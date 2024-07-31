#Calculator_Project
import tkinter as tk
def click(event):
    global expression
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(expression))
            expression_var.set(result)
            expression = result
        except Exception as e:
            expression_var.set("Error")
            expression = ""
    elif text == "C":
        expression = ""
        expression_var.set("")
    else:
        expression += text
        expression_var.set(expression)
root = tk.Tk()
root.title("Calculator")

expression = ""
expression_var = tk.StringVar()

entry = tk.Entry(root, textvar=expression_var, font="lucida 20 bold", borderwidth=5, relief="sunken")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'
]
row, col = 1, 0
for button in buttons:
    b = tk.Button(root, text=button, font="lucida 15 bold", padx=20, pady=20)
    b.grid(row=row, column=col, padx=5, pady=5)
    b.bind("<Button-1>", click)
    col += 1
    if col == 4:
        col = 0
        row += 1

root.mainloop()
