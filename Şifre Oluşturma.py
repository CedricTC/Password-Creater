import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import string

def parola():
    min_length = int(length_entry.get())

    if min_length < 6:
        messagebox.showwarning("Uyarı", "Parola uzunluğu en az 6 karakter olmalıdır.")
        return

    has_numbers = number_var.get()
    has_special_characters = special_var.get()

    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if has_numbers:
        characters += digits
    if has_special_characters:
        characters += special

    password = ''.join(random.choice(characters) for _ in range(min_length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

  



root = tk.Tk()
root.title("Parola Oluşturucu")


length_label = ttk.Label(root, text="Parola Uzunluğu:",)
length_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

length_entry = ttk.Entry(root)
length_entry.grid(row=0, column=1, padx=5, pady=5)
length_entry.insert(0, "6")


number_var = tk.BooleanVar()
number_check = ttk.Checkbutton(root, text="Rakamlar", variable=number_var)
number_check.grid(row=1, column=0, padx=5, pady=5, sticky="w")
number_check.invoke()


special_var = tk.BooleanVar()
special_check = ttk.Checkbutton(root, text="Özel Karakterler", variable=special_var)
special_check.grid(row=2, column=0, padx=5, pady=5, sticky="w")
special_check.invoke()


generate_button = ttk.Button(root, text="Parola Oluştur", command=parola)
generate_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)


password_label = ttk.Label(root, text="Oluşturulan Parola:")
password_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")

password_entry = ttk.Entry(root, width=30)
password_entry.grid(row=4, column=1, padx=5, pady=5)


root.mainloop()
