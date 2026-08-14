#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

PLACEHOLDER = "[name]"
    
with open("./Input/Names/invited_names.txt") as name_data:
    name_list = name_data.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_template:
    for name in name_list:
        letter_body = letter_template.read()
        letter_body = letter_body.replace(PLACEHOLDER, f"{name.strip()}")
        with open(f"./Output/ReadyToSend/letter_for_{name.strip()}.txt", mode="w") as send_letter:
            send_letter.write(letter_body)

