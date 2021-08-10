from tkinter import *

window = Tk()
window.title("My First GUI Program")

window.minsize(width=500, height=300)

# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))

my_label.pack()
# my_label["text"] = "New Text"
my_label.config(text="New Text")

# Entry: An input component
input_entry = Entry(width=10)

input_entry.pack()


# Button
def button_clicked():
    text_input = input_entry.get()
    my_label.config(text=text_input)
    print("I got clicked!")


button = Button(text="Click Me", command=button_clicked)
button.pack()


window.mainloop()
