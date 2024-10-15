import tkinter as tk
from math import sqrt

def click(event):
    current = entry.get()
    button_text = event.widget.cget("text")

    if button_text == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

def square_root():
    try:
        current = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, sqrt(current))
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def exponent():
    entry.insert(tk.END, "**")

root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("400x500")

main_frame = tk.Frame(root, bg="black", relief="solid", borderwidth=5)
main_frame.pack(padx=10, pady=10, fill="both", expand=True)

entry = tk.Entry(main_frame, width=25, font="Arial 18", borderwidth=5, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, col) in buttons:
    button = tk.Button(main_frame, text=text, font="Arial 14", padx=20, pady=20, borderwidth=3, relief="ridge")
    button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    button.bind("<Button-1>", click)

sqrt_button = tk.Button(main_frame, text="√", font="Arial 14", padx=20, pady=20, borderwidth=3, relief="ridge", command=square_root)
sqrt_button.grid(row=5, column=0, padx=5, pady=5, sticky="nsew")

exp_button = tk.Button(main_frame, text="x^y", font="Arial 14", padx=15, pady=20, borderwidth=3, relief="ridge", command=exponent)
exp_button.grid(row=5, column=1, padx=5, pady=5, sticky="nsew")

for i in range(6):
    main_frame.grid_rowconfigure(i, weight=1)
for i in range(4):
    main_frame.grid_columnconfigure(i, weight=1)

root.mainloop()
