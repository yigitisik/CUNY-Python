from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=100)


equal_text = Label(text="is equal to", font=("Arial", 12, "bold"))
equal_text.grid(row=1,column=0,padx=10)

miles_text = Label(text="Miles", font=("Arial", 12, "bold"))
miles_text.grid(row=0,column=2)

km_text = Label(text="Km", font=("Arial", 12, "bold"))
km_text.grid(row=1,column=2)

miles_input = Entry(width=5)
miles_input.grid(row=0,column=1)
miles_input.focus()
miles_input.insert(0, "0")


km_output = Label(text="0")
km_output.grid(row=1,column=1)

def convert_miles_to_km():
    try:
        mile = float(miles_input.get())
        converted_value_in_km =  round(mile*1.609, ndigits=2)
        km_output.config(text = f"{converted_value_in_km}")
    except ValueError:
        km_output.config(text= "Value Error")


calculate_button = Button(text="Convert", command=convert_miles_to_km)
calculate_button.grid(row=3, column=1)

#Let users hit Enter to convert, not just click button
window.bind("<Return>", lambda event: convert_miles_to_km())
window.mainloop()

