from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)

# username entry
username_entry = Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2)

# password entry
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# generate password button
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3, column=2)

# Add button
add_button = Button(text="Add", width=36)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
