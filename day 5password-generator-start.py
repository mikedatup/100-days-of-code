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


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password = ""

number_of_letters = int(len(letters)) - 1
for letter in range(1, nr_letters + 1):
  curent_symb = letters[random.randint(0,number_of_letters)]
  password += curent_symb
  
number_of_numbers = int(len(numbers)) - 1
for letter in range(1, nr_numbers + 1):
  curent_symb = numbers[random.randint(0,number_of_numbers)]
  password += curent_symb

number_of_symbols = int(len(symbols)) - 1
for letter in range(1, nr_symbols + 1):
  curent_symb = symbols[random.randint(0,number_of_symbols)]
  password += curent_symb

#pass_count = int(len(letters))

print(password)


l = list(password)

random.shuffle(l)
password = ''.join(l)

print(password)

#letters1 = 0
#symbols1 = 0
#numbers1 = 0

#letters1.append("dof")

#print(letters1)
#print(symbols1)
#print(numbers1)
