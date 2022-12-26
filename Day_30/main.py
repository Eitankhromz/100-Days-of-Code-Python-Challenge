from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for char in range(randint(8, 10))]
    password_list += [choice(symbols) for char in range(randint(2, 4))]
    password_list += [choice(numbers) for char in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(END, string=password)
    window.clipboard_clear()
    window.clipboard_append(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
            }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please do not leave any empty fields")
    else:
        try:
            with open("data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file) #json.load returns anything in the file as a dictionary
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()

    try:
        with open("data.json", "r") as data_file:
            websites = json.load(data_file)
    except FileNotFoundError:
        messagebox.showwarning("Oops", "No Data File Found")
    else:
        if website in websites:
            email = websites[website]["email"]
            password = websites[website]["password"]
            messagebox.showinfo(website, f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showwarning("Oops", f"No Details For {website} Exists")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

bg_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=bg_img)
canvas.grid(row=0, column=1)

# WEBSITE_____________________________________
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry(width=21)
website_entry.insert(END, string="Enter Website")
website_entry.focus()
website_entry.grid(row=1, column=1, sticky=EW)

# USERNAME/EMAIL _____________________________________
username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)

username_entry = Entry(width=35)
username_entry.insert(END, string="email@gmail.com")
username_entry.grid(row=2, column=1, columnspan=2, sticky=EW)

# PASSWORD_____________________________________
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=21)
password_entry.insert(END, string="Enter Password")
password_entry.grid(row=3, column=1, sticky=EW)

generate_password_button = Button(text="Generate Password", width=15, command=password_generator)
generate_password_button.grid(row=3, column=2)
generate_password_button.config(padx=20)

add_info_button = Button(text="Add", width=36, command=save)
add_info_button.grid(row=4, column=1, columnspan=2, sticky=EW)

search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(row=1, column=2, sticky=NSEW)


window.mainloop()
