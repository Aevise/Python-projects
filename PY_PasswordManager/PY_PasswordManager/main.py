from tkinter import *
import os
from tkinter import messagebox, simpledialog
from password_generator import generate_password
import pyperclip
import json


CANVAS_HEIGHT = 200
CANVAS_WIDTH = 200
LOGO = "./logo.png"
EMAIL = "meteo212@gmail.com"
TXT_FILE = "./data.txt"
JSON_FILE = "./data.json"

# -------------------------------------- methods ---------------------------------
def save_password()->None:
    """Writes data to the file if all entries are typed in.
    """
    web_info = website_entry.get().capitalize()
    user_info = user_entry.get()
    pass_info = password_entry.get()
    json_data = {
        web_info: {
            "email": user_info,
            "password": pass_info
        }
    }
    if web_info != "" and user_info != "" and pass_info != "":
        decision = messagebox.askokcancel(title = "Entered details", message = f"Entered details:\nWebsite: {web_info}\nEmail/Username: {user_info}\nPassword: {pass_info}\nIs it correct?")
        if decision:
            with open(TXT_FILE, mode = "a") as file:
                file.write(f"{web_info} | {user_info} | {pass_info}\n")
            try:
                with open(JSON_FILE, "r") as file:
                    #read old data
                    data = json.load(file)
                    #update old data
                    data.update(json_data)
            except FileNotFoundError:
                with open(JSON_FILE, "w") as file:
                    #create new file and dump data
                    json.dump(json_data, file, indent = 4)
            else:
                with open(JSON_FILE, "w") as file:
                    #save updated data
                    json.dump(data, file, indent = 4)
            finally:
                messagebox.showinfo(title = "Success", message = "Data entered successfully.")
                website_entry.delete(0, END)
                password_entry.delete(0, END)  
    else:
        messagebox.showinfo(title = "Failure", message = "Please fill in all the entries.")

#-----------------------------------------------------------------------------------------------------------------------------------------

def delete_data()->None:
    """Deletes your saved passwords
    """
    decision = messagebox.askokcancel(title = "Data Eraser", message = f"Are you sure you want to remove all your data?\nThis process can not be reversed.")
    if decision:
        try:
            os.remove(TXT_FILE)
            messagebox.showinfo(title = "Success", message = "Txt data destroyed.")
        except FileNotFoundError:
            messagebox.showerror(title = "Failure", message = "No txt data to destroy.")
        try:
            os.remove(JSON_FILE)
            messagebox.showinfo(title = "Success", message = "JSON data destroyed.")
        except FileNotFoundError:
            messagebox.showerror(title = "Failure", message = "No JSON data to destroy.")       

#-----------------------------------------------------------------------------------------------------------------------------------------

def random_password()->None:
    """Ask user if he wants to generate a password using standard range of values or if he wants to customize them.
    Copies generated password to the users clipboard.
    """
    new_password = []
    decision = messagebox.askyesno(title = "Random Password Generator", message = "Do you want to customize random password generator?\n"
            "Minimum number of letters in the password. Defaults to 8.\n"
            "Maximum number of letters in the password. Defaults to 10.\n"
            "Minimum number of symbols in the password. Defaults to 2.\n"
            "Maximum number of symbols in the password. Defaults to 4.\n"
            "Minimum number of numbers in the password. Defaults to 2.\n"
            "Maximum number of numbers in the password. Defaults to 4.")
    password_entry.delete(0, END)
    if decision:
        min_letters = simpledialog.askinteger(title = "Letters", prompt = "Minimum number of letters in the password:") 
        max_letters = simpledialog.askinteger(title = "Letters", prompt = "Maximum number of letters in the password:")
        while max_letters < min_letters:
            messagebox.showerror(title  = "Error", message = "Maximum value can not be lower than the minimum value.\nTry Again.")
            max_letters = simpledialog.askinteger(title = "Letters", prompt = "Maximum number of letters in the password:")
        min_symbols = simpledialog.askinteger(title = "Symbols", prompt = "Minimum number of symbols in the password:") 
        max_symbols = simpledialog.askinteger(title = "Symbols", prompt = "Maximum number of symbols in the password:") 
        while max_symbols < min_symbols:
            messagebox.showerror(title  = "Error", message = "Maximum value can not be lower than the minimum value.\nTry Again.")
            max_symbols = simpledialog.askinteger(title = "Symbols", prompt = "Maximum number of symbols in the password:") 
        min_numbers = simpledialog.askinteger(title = "Numbers", prompt = "Minimum number of numbers in the password:") 
        max_numbers = simpledialog.askinteger(title = "Numbers", prompt = "Maximum number of numbers in the password:") 
        while max_numbers < min_numbers:
            messagebox.showerror(title  = "Error", message = "Maximum value can not be lower than the minimum value.\nTry Again.")
            max_numbers = simpledialog.askinteger(title = "Numbers", prompt = "Maximum number of numbers in the password:") 
        new_password = generate_password(min_letters, max_letters, min_symbols, max_symbols, min_numbers, max_numbers)
    else:
        new_password = generate_password()
    password_entry.insert(0, new_password)
    pyperclip.copy(new_password)
    messagebox.showinfo(title = "Success", message = "Password successfully generated and copied to your clipboard.")

#-----------------------------------------------------------------------------------------------------------------------------------------
def search_data():
    website = website_entry.get().capitalize()
    if(website != ""):
        try:
            with open(JSON_FILE, "r") as file:
                data = json.load(file)     
                if(website in data):
                    data_keys = list(data[website].keys())
                    messagebox.showinfo(title = f"{website}", message = f"{data_keys[0]}: {data[website][data_keys[0]]}\n{data_keys[1]}: {data[website][data_keys[1]]}")
                else:
                    messagebox.showinfo(title = "Error", message = f"No data found regarding {website} website")
        except FileNotFoundError:
            messagebox.showerror(title = "Error", message = "No data found.")  
    else:
        messagebox.showerror(title = "Error", message = "Please fill in the label first.")
#-----------------------------------------------------------------------------------------------------------------------------------------

# ------------------------ UI Setup ----------------------------------
window = Tk()
window.title("Password Manager")
window.config(padx = 50, pady = 50)

canvas = Canvas(width = CANVAS_WIDTH, height = CANVAS_HEIGHT)
logo_image = PhotoImage(file = LOGO)
canvas.create_image(CANVAS_WIDTH//2, CANVAS_HEIGHT//2, image = logo_image)
canvas.grid(column = 1, row = 0)

    # --------------------------- Labels -----------------------------------
website_label = Label(text = "Website:", pady = 5)
website_label.grid(column = 0, row = 1)

user_label = Label(text = "Email/Username:", pady = 5)
user_label.grid(column = 0, row = 2)

password_label = Label(text = "Password:", pady = 5)
password_label.grid(column = 0, row = 3)

    # -------------------------- Entries -------------------------------------
website_entry = Entry(width = 33)
website_entry.grid(column = 1, row = 1)
website_entry.focus() #cursor start on this location

user_entry = Entry(width = 52)
user_entry.grid(column = 1, row = 2, columnspan = 2)
user_entry.insert(0, EMAIL)

password_entry = Entry(width = 33)
password_entry.grid(column = 1, row = 3)

    # -------------------------- Buttons ------------------------------------
add_button = Button(text = "Add", width = 44, highlightthickness = 0, command = save_password)
add_button.grid(column = 1, row = 4, columnspan = 2)

generate_button = Button(text = "Generate Password", highlightthickness = 0, command = random_password)
generate_button.grid(column = 2, row = 3)

clear_button = Button(text = "Clear Data", command = delete_data)
clear_button.grid(column = 2, row = 0)

search_button = Button(text = "Search", highlightthickness = 0, width = 14, command = search_data)
search_button.grid(column = 2, row = 1)

window.mainloop()