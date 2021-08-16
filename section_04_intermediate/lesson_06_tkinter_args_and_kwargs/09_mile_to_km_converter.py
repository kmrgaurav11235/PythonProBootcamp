from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

miles_entry = Entry(width=7)
miles_entry.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(row=1, column=0)

km_calculated_label = Label(text="0")
km_calculated_label.grid(row=1, column=1)

km_text_label = Label(text="Km")
km_text_label.grid(row=1, column=2)


def calculate_miles_to_km():
    miles = float(miles_entry.get())
    km = round(1.609344 * miles, 2)
    km_calculated_label.config(text=km)


calculate_button = Button(text="Calculate", command=calculate_miles_to_km)
calculate_button.grid(row=2, column=1)

window.mainloop()
