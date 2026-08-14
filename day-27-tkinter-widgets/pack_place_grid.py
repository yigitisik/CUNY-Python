#pack() does packing automatically
#place() requires x-y coords and specific
#grid() is a good balance in between

from tkinter import *

def button_clicked():
    print("button_clicked")

window = Tk()
window.title("GUI Program")
window.minsize(width=500, height=300)
window.config(padx=300, pady=30)

#label
my_label = Label(text="This is a label", font=('Arial', 24, "bold"))
my_label.config(text="this is a new label")
my_label.grid(column=0,row=0)

#button
my_button = Button(text="Button", command=button_clicked)
my_button.grid(column=1, row=1)

#entry
my_input = Entry(width=10)
print(my_input.get())
my_input.grid(column=3, row=2)

#second button
second_button = Button(text="2nd Button", command=button_clicked)
second_button.grid(column=2,row=0)

window.mainloop()
