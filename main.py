from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)
    password = "".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)
# --------------------------SEARCH PASSWORD---------------------------------#
def search_password():
    web_search = web_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if web_search in data:
            user_search = data[web_search]["user"]
            pass_search = data[web_search]["password"]
            messagebox.showinfo(title=web_search, message=f"Email: {user_search}"
                                                  f" \n Password: {pass_search}")
        else:
            messagebox.showinfo(title="Error", message=f"No passwords"
                                                       f" were found for this website: {web_search}")




# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = web_entry.get()
    user = mail_entry.get()
    password = pass_entry.get()
    new_data={
        website: {
            "user": user,
            "password": password,
        }
    }

    if website=="" or password=="":
        messagebox.showerror(title="Error", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        except json.decoder.JSONDecodeError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            web_entry.delete(0, END)
            pass_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

label1 = Label(text="Website:")
label1.grid(row=1, column=0)
label2 = Label(text="Email/Username:")
label2.grid(row=2, column=0)
label3 = Label(text="Password:")
label3.grid(row=3, column=0)

web_entry = Entry()
web_entry.grid(row=1, column=1, sticky="EW")
web_entry.focus()
mail_entry = Entry()
mail_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
mail_entry.insert(0, "tfm14102003@gmail.com")
pass_entry = Entry()
pass_entry.grid(row=3, column=1, sticky="EW")

button1 = Button(text="Generate Password", highlightthickness=0, command=password_generator)
button1.grid(row=3, column=2, sticky="EW")
button2 = Button(text="Add", width=36, highlightthickness=0, command=save_password)
button2.grid(row=4, column=1, columnspan=2, sticky="EW")
button3 = Button(text="Search", highlightthickness=0, command=search_password)
button3.grid(row=1, column=2, sticky="EW")




mainloop()