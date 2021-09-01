from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- CONSTANTS ------------------------------- #
DATA_FILE_NAME = "data.json"
USER_NAME_FIELD = "user_name"
PASSWORD_FIELD = "password"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_list = []

    password_list.extend([choice(letters) for _ in range(nr_letters)])
    password_list.extend([choice(symbols) for _ in range(nr_symbols)])
    password_list.extend([choice(numbers) for _ in range(nr_numbers)])

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(index=0, string=password)

    # Copy password to clipboard
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    # Get data
    website = website_entry.get()
    user_name = username_entry.get()
    user_password = password_entry.get()

    if len(website) == 0 or len(user_name) == 0 or len(user_password) == 0:
        messagebox.showerror(title="Oops!", message="Please don't leave any fields empty!")
    else:
        confirmation_message = f"These are the details entered: \n  User/Email: {user_name} " \
                               f"\n  Password: {user_password}\nIs this ok to save?"

        is_ok = messagebox.askokcancel(title=website, message=confirmation_message)  # Confirmation dialog box
        if is_ok:
            data_dict = {
                website: {
                    USER_NAME_FIELD: user_name,
                    PASSWORD_FIELD: user_password,
                }
            }

            try:
                with open(file=DATA_FILE_NAME, mode="r") as data_file:
                    # Read the data
                    file_data = json.load(fp=data_file)

                    # Update the file_data with the new data in data_dict
                    file_data.update(data_dict)
            except FileNotFoundError:
                # File doesn't exists
                file_data = data_dict

            # Save the data
            with open(file=DATA_FILE_NAME, mode="w") as data_file:
                json.dump(obj=file_data, fp=data_file, indent=4)

            # Clear widgets
            website_entry.delete(first=0, last=END)
            password_entry.delete(first=0, last=END)
            website_entry.focus()

# ---------------------------- SEARCH DATA ------------------------------- #


def search_data():
    website = website_entry.get()
    if len(website) == 0:
        messagebox.showerror(title="Oops!", message="Please provide Website for Search!")
    else:
        try:
            with open(file=DATA_FILE_NAME, mode="r") as data_file:
                file_data = json.load(fp=data_file)
        except FileNotFoundError:
            messagebox.showerror(title="Oops!", message="No Data File Found!")
        else:
            if website in file_data:
                website_details = file_data[website]
                messagebox.showinfo(title=website,
                                    message=f"User/Email: {website_details[USER_NAME_FIELD]}"
                                            f"\nPassword: {website_details[PASSWORD_FIELD]}")
            else:
                messagebox.showwarning(title="Oops!", message="No details for website exists!")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
logo_image = PhotoImage(file="logo.png")
canvas = Canvas(height=200, width=200)
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# website label
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

# username label
username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)

# password label
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# website entry
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()  # Put the cursor here

# username entry
username_entry = Entry(width=38)
username_entry.insert(index=0, string="kgaurav@email.com")  # Insert default text at the begining
username_entry.grid(row=2, column=1, columnspan=2)

# password entry
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# search button
search_button = Button(text="Search", width=13, command=search_data)
search_button.grid(row=1, column=2)

# generate password button
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

# Add button
add_button = Button(text="Add", width=36, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
