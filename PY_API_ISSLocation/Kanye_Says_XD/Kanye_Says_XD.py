from tkinter import *
import requests

WEBSITE = "https://api.kanye.rest"

def get_quote():
    data = get_data()
    canvas.itemconfig(quote_text, text = f"{data['quote']}")

def get_data():
    response = requests.get(url = WEBSITE)
    response.raise_for_status()
    data = response.json()
    return data

window = Tk()
window.title("Kanye Says XD")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanyeXD_img = PhotoImage(file="kanye.png")
kanyeXD_button = Button(image=kanyeXD_img, highlightthickness=0, command=get_quote)
kanyeXD_button.grid(row=1, column=0)



window.mainloop()