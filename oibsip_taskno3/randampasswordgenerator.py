import string as s
import random as r
import tkinter as t
import pyperclip

def randomgenerator(g):
    k = list(s.ascii_letters + s.digits + s.punctuation)
    return "".join(r.sample(k, g))

def generate_password():
    g_str = length_entry.get()
    if not g_str.isdigit():
        error_label.config(text="Error: Please enter a valid password length")
        return

    g = int(g_str)
    if g == 0 or g>20:
        error_label.config(text="Error: Password length cannot be zero or Greater than 20")
        return

    result = randomgenerator(g)
    pyperclip.copy(result)
    result_label.config(text=f"Generated Password: {result}")
    error_label.config(text="")

Pass = t.Tk()
Pass.title("Randomly Password Generator")

length_label = t.Label(Pass, text="Length of Password:")
length_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

length_entry = t.Entry(Pass)
length_entry.grid(row=0, column=1, padx=10, pady=10, sticky="we")

generate_button = t.Button(Pass, text="Generate Password", command=generate_password)
generate_button.grid(row=1, column=0, columnspan=2, pady=10)

copy_button = t.Button(Pass, text="Copy to Clipboard", command=lambda: pyperclip.copy(result_label.cget("text").split(": ")[1]))
copy_button.grid(row=2, column=0, columnspan=2, pady=10)

result_label = t.Label(Pass, text="")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

error_label = t.Label(Pass, text="", fg="red")
error_label.grid(row=4, column=0, columnspan=2, pady=10)

Pass.mainloop()
