from tkinter import *

window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

#LABEL
label = Label(text="This is old text")
label.config(text="This is new text")
label.pack()

#BUTTONS
def action():
    print("Do something")

#Calls action when pressed
button = Button(text="Click me", command=action())
button.pack()

#ENTRY
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
entry.pack()


#TEXT
text = Text(height=5, width=30)
#Puts cursor in textbox
text.focus()
#Adds some text to begin with
text.insert(END, "Example of mult-line text entry.")
#Gets current value of the textbox at line 1 character 0
print(text.get("1.0", END))
text.pack()

#SPINBOX
def spinbox_used():
    #Gets current value in spinbox
    print(spinbox.get())

spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#SCALE
#Called with current scale value
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#CHECKBUTTON
def checkbutton_used():
    #Prints 1 if ON button checked, otherwise 0
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is on?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


#RADIOBUTTON
def radio_used():
    print(radio_state.get())

radio_state = IntVar()
radio_button1 = Radiobutton(text="Option 1", value=1, variable=radio_state, command=radio_used)
radio_button2 = Radiobutton(text="Option 2", value=0, variable=radio_state, command=radio_used)
radio_button1.pack()
radio_button2.pack()


#LISTBOX
def listbox_used(event):
    #Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apples", "Pear", "Orange", "Bananas"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


window.mainloop()
