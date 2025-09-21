from tkinter import *
import requests
API_ENDPOINT = "https://api.breakingbadquotes.xyz/v1/quotes"

def get_quote():
    api_resp = requests.get(API_ENDPOINT)
    api_resp.raise_for_status()

    data = api_resp.json()
    author = data[0]["author"]
    quote = data[0]["quote"]
    return [author, quote]

br_ba_quote = get_quote()
#UI SETUP
window = Tk()
window.title(f"{br_ba_quote[0]} Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text=br_ba_quote[1], width=250, font=("Arial", 24, "bold"), fill="white")
canvas.grid(row=0, column=0)

br_ba_img = PhotoImage(file="br_ba.png")
br_ba_button = Button(image=br_ba_img, highlightthickness=0, command=get_quote)
br_ba_button.grid(row=1, column=0)

window.mainloop()