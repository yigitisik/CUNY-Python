import json
from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#used once in save_pw function and once in pw_input initialization to generate the first pw
def create_pw():
    pw_letter_list = [choice(letters) for char in range(randint(8, 10))]
    pw_num_list = [choice(numbers) for char in range(randint(2, 4))]
    pw_symbol_list = [choice(symbols) for char in range(randint(2, 4))]
    pw_list = pw_letter_list + pw_num_list + pw_symbol_list
    shuffle(pw_list)
    #copy to clipboard
    pyperclip.copy("".join(pw_list))
    return "".join(pw_list)
def save_pw():
    generated_pw = create_pw()
    #copy to clipboard
    pyperclip.copy(generated_pw)
    pw_input.delete(0,END)
    pw_input.insert(0,generated_pw)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_new_pw_to_records():
#set structure for saving data
    website = website_input.get()
    email = email_username_input.get()
    pw = pw_input.get()
    new_data = {
        website: {
            "email": email,
            "pw": pw
        }
    }
    #check for missing input
    if len(website)==0 or len(pw)==0 or len(email)==0:
        messagebox.showerror(title="Missing Input", message="Please fill out all empty fields before clicking add.")
        return
    else:
    #     is_ok_to_save = messagebox.askokcancel(title=website, message=f"Please confirm below is what you entered\n"
    #                                                                   f"Email: {email}\nPassword: {pw}\nIs this okay to save?")
    #     if is_ok_to_save:
        #try finding and reading data
        try:
            with open("data.json", "r") as data_file:
                json_data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("data.json", "w") as data_file:
                json_data.update(new_data)
                json.dump(json_data, data_file, indent=4)
        #delete the content in the input boxes of GUI
        finally:
                website_input.delete(0, END)
                pw_input.delete(0, END)
def search_pw():
    website = website_input.get()
    try:
        with open("data.json", "r") as data_file:
            json_data = json.load(data_file)
    except FileNotFoundError as searched_file:
        messagebox.showinfo(title="Not found a file", message=f"No file found based on search of {searched_file}")
    else:
        if website in json_data:
            email = json_data[website]["email"]
            pw = json_data[website]["pw"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {pw}")
        else:
            messagebox.showinfo(title="Not found a website", message=f"No web site found based on search of {website}")
# ---------------------------- UI SETUP ------------------------------- #
#window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#image
canvas = Canvas(width=200, height=200)
image_path = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=image_path)
canvas.grid(row=0,column=1)

#labels
website_label = Label(text= "Website:")
website_label.grid(row=1, column=0)
email_username_label = Label(text= "Email/Username:")
email_username_label.grid(row=2, column=0)
pw_label = Label(text="Password:")
pw_label.grid(row=3, column=0)

#entries/inputs
website_input = Entry(width=21, takefocus=1)
website_input.grid(row=1, column=1)
website_input.focus()

email_username_input = Entry(width=38)
email_username_input.grid(row=2, column=1, columnspan=2)
email_username_input.insert(0, "youremail@domain.com")

pw_input = Entry(width=21)
pw_input.grid(row=3, column=1)
initial_generated_pw = create_pw()
pw_input.insert(0, initial_generated_pw)

#buttons
generate_pw_button = Button(text="Generate Password", command=save_pw, width=12)
generate_pw_button.grid(row=3, column=2)
add_button = Button(text="Add", width=38, command=add_new_pw_to_records)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", command=search_pw, width=12)
search_button.grid(row=1, column=2)

window.mainloop()