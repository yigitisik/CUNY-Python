#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
easy_pw_string = ""
for char in range(1, nr_letters + 1):
  easy_pw_string += random.choice(letters)
for char in range(1, nr_symbols + 1):
  easy_pw_string += random.choice(symbols)
for char in range(1, nr_numbers + 1):
  easy_pw_string += random.choice(numbers)
print(easy_pw_string)  

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
hard_pw_string = ""
allcharacters = []
for char in range(1, nr_letters + 1):
  allcharacters.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  allcharacters += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  allcharacters += random.choice(numbers)

# to show conceptual way of what shufffling does:

#totalnumberofcharacters = nr_letters + nr_symbols + nr_numbers
#for i in range(1, totalnumberofcharacters + 1):
#  hard_pw_string += allcharacters[random.randint(0, len(allcharacters)-1)]

# of course easy way below:
random.shuffle(allcharacters)
for char in allcharacters:
  hard_pw_string += char
print(hard_pw_string)  