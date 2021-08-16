from tkinter import *

window = Tk()
window.title("Layout Exercise")
window.minsize(width=500, height=300)

# Add Padding
window.config(padx=30, pady=30)

# Divide screen in 3 x 4 grid

# Label (0,0)
label = Label(text="Exercise Label", font=("Arial", 24, "bold"))
label.grid(row=0, column=0)

# Button (1, 1)
button = Button(text="Click Me")
button.grid(row=1, column=1)

# New Button (0, 2)
new_button = Button(text="Click Me too!")
new_button.grid(row=0, column=2)

# Entry (2, 3)
entry = Entry()
entry.grid(row=2, column=3)

window.mainloop()