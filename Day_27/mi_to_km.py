from tkinter import *


def convert():
    km = float(entry.get()) * 1.609
    kilometers.config(text=f"{km}")


window = Tk()
window.title("Mi to Km Converter")
window.minsize(width=200, height=100)
window.config(pady=20, padx=20)

#Create labels
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

is_equal_label = Label(text="is equal to ")
is_equal_label.grid(column=0, row=1)

kilometers = Label(text="0")
kilometers.grid(column=1, row=1)

#Create entrybox
entry = Entry(width=10)
entry.grid(column=1, row=0)

#Create Button
calculate_button = Button(text="Calulate", command=convert)
calculate_button.grid(column=1, row=2)

window.mainloop()
