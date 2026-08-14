from tkinter import *
window = Tk()
window.title("GUI Game")
window.minsize(width=800, height=600)

label = Label(text= "Testing label", font=("Calibri",24))
label.pack()

inputted = Entry(width=20)
inputted.pack()

def button_click():
    value_inputted = inputted.get()
    label["text"] = value_inputted
    # OR label.config(text="Button was clicked.")

button = Button(text="Okay", command=button_click)
button.pack()

window.mainloop()

