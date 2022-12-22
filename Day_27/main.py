from tkinter import *


def button_clicked():
    print("I got clicked")
    my_label.config(text=input.get())


window = Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)

#LABEL
my_label = Label(text="I am a lablel", font=("Arial", 24, "bold"))
my_label.pack(side="bottom", expand=True)

#CHANGING TEXT
my_label["text"] = "New Text"
my_label.config(text="New TExt")


button = Button(text="Click Me", command=button_clicked)
button.pack()

#ENTRY
input = Entry(width=10)
input.pack()







window.mainloop()
