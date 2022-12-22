from tkinter import *


def button_clicked():
    print("I got clicked")
    my_label.config(text=input.get())


window = Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#LABEL
my_label = Label(text="I am a lablel", font=("Arial", 24, "bold"))
#CHANGING TEXT
my_label["text"] = "New Text"
my_label.config(text="New Text")
# my_label.pack(side="bottom", expand=True)
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)


button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

#ENTRY
input = Entry(width=10)
# input.pack()
input.grid(column=3, row=3)

new_button = Button(text="I am a new button")
new_button.grid(column=2, row=0)





window.mainloop()
