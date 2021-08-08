import tkinter

window = tkinter.Tk()  # Create a new window
window.title("My First GUI Program")

# The size of the window will adjust automatically to fit all the components. However, we can set a minimum size
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))

# https://docs.python.org/3/library/tkinter.html#the-packer
my_label.pack()  # Place the label on the screen and automatically centre it.
# my_label.pack(side="left")
# my_label.pack(expand=True)

# Keeps the program from stopping. This is always at the end.
window.mainloop()
