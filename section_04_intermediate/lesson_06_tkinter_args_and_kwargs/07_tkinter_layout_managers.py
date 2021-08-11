from tkinter import *

window = Tk()
window.title("My First GUI Program")

window.minsize(width=500, height=300)

my_label = Label(text="I am a label", font=("Arial", 24, "bold"))

# Tkinter has many different layout managers. If a widget is added in code but it doesn't have any layout specified,
# it will not show up. The 3 important layouts are:
# 1. Pack -> Packs everything from the top. We can also use side="left/right/bottom" to pack from other sides
# my_label.pack()
# 2. Place -> Specify the x and y coordinates of the widget. (x=0, y=0) is the top left.
# my_label.place(x=100, y=200)
# 3. Grid -> Divides the window into a grid and lets you specify the row and column
my_label.grid(row=5, column=5)
# Warning: You cannot mix-up grid() and pack() in the same program.


def button_clicked():
    my_label.config(text="Button clicked!")
    print("I got clicked!")


button = Button(text="Click Me", command=button_clicked)
button.grid(row=2, column=2)


window.mainloop()