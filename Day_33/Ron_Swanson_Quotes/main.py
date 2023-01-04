from tkinter import *
import requests


def get_quote():
    """Retrieves quote from API and..."""
    response = requests.get(url="https://ron-swanson-quotes.herokuapp.com/v2/quotes")

    #Raise exception
    response.raise_for_status()

    swanson_quote = response.json()[0]

    canvas.itemconfig(quote_text, text=swanson_quote)



window = Tk()
window.title("Swanson Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Swanson Quote Goes HERE", width=250, font=("Arial", 30, "bold"),
                                fill="white")
canvas.grid(row=0, column=0)

ron_img = PhotoImage(file="ron-swanson.png")
ron_button = Button(image=ron_img, highlightthickness=0, command=get_quote)
ron_button.grid(row=1, column=0)



window.mainloop()
