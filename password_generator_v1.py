import random
import string
import pyperclip
from tkinter import *
from tkinter.ttk import *
 
# Function for calculation of password
def set_password():
    # Clear entry
    entry.delete(0, END)
 
    # Get the length of password
    length = var1.get()

    # Create letters, numbers and punctuation for password
    letters = string.ascii_letters
    numbers = string.digits
    punctuation = string.punctuation
 
    # if strength selected is Low
    if var.get() == 1:
        simple_random = ''.join(random.choice(letters) for _ in range(length))
        return simple_random
 
    # if strength selected is Medium
    elif var.get() == 0:
        medium_random = ''.join(random.choice(letters + numbers) for _ in range(length))
        return medium_random
 
    # if strength selected is Strong
    elif var.get() == 3:
        strong_random = ''.join(random.choice(letters + numbers + punctuation) for _ in range(length))
        return strong_random
    else:
        print("Please choose an option")
 
# Convert pass into hex
def hexadecimal_pass(data):
    # Clear entry
    entry_hex.delete(0, END)

    # Encode data 
    # Convert it into hex and return
    utf_value = data.encode('utf=8')
    hex_data = utf_value.hex()
    return hex_data

# Function for generation of password
def generate():
    # Get password and insert
    create_pass = set_password()
    entry.insert(10, create_pass)

    # Get hex from password and insert 
    data_inhex = hexadecimal_pass(create_pass)
    entry_hex.insert(33,data_inhex)

# Function for copying password to clipboard
def copy_password():
    random_password = entry.get()
    pyperclip.copy(random_password)
 
def clear_data():
    entry_hex.delete(0, END)
    entry.delete(0, END)
    
# Main Function
# Create GUI window
# Set values for settings
root = Tk()
root.title("Password Generator - Version 1.0")
root.geometry("540x200")
root.resizable(width=0, height=0)
var = IntVar()
var1 = IntVar()

# Hello text lable
Text_start = Label(root, text="> Generate your password <",font=("Arial", 12, "bold"))
Text_start.grid(row=0,column=1,columnspan=3,padx=15, pady=15)

# Create label and entry for password
Random_password = Label(root, text="Password",font=("Arial",10))
Random_password.grid(row=2, padx=10, pady=10)
entry = Entry(root,width=33)
entry.grid(row=2, column=1, padx=10, pady=10)

# Create label and entry for hexadecimal
Show_hexadecimal = Label(root, text="Hexadecimal",font=("Arial",10))
Show_hexadecimal.grid(row=3, padx=5, pady=5, columnspan=1)
entry_hex = Entry(root, width=64)
entry_hex.grid(row=3, column=1, padx=5, pady=5, columnspan=3)
 
# Create label for length of password
c_label = Label(root, text="Length")
c_label.grid(row=1, column=0, columnspan=1)

# Create Buttons Copy which will copy
copy_button = Button(root, text="Copy", command=copy_password)
copy_button.grid(row=2, column=2)

# Create Buttons which will generate password
generate_button = Button(root, text="Generate", command=generate)
generate_button.grid(row=2, column=3)

# Create Buttons which will clear entry
clear_button = Button(root, text="Clear", command=clear_data)
clear_button.grid(row=4, column=2, columnspan=2)
 
# Radio Buttons for deciding the strength of password
# Default strength is Medium
radio_low = Radiobutton(root, text="Low", variable=var, value=1)
radio_low.grid(row=1, column=1, columnspan=1, sticky='E')
radio_middle = Radiobutton(root, text="Middle", variable=var, value=0)
radio_middle.grid(row=1, column=1, columnspan=2, sticky='E')
radio_strong = Radiobutton(root, text="Strong", variable=var, value=3)
radio_strong.grid(row=1, column=1, columnspan=3, sticky='E')
combo = Combobox(root, textvariable=var1, width=15)
 
# ComboBox for length of your password
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16,
                   17, 18, 19, 20, 21, 22, 23, 24, 25,
                   26, 27, 28, 29, 30, 31, 32)
combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.grid(column=0, row=1, columnspan=2)

# start the GUI prog
root.mainloop()