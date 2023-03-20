# Import the random module here

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

import random

number_of_people = int(len(names)) - 1
lucky_person = random.randint(0,number_of_people)

print(f" {names[lucky_person]} is going to buy the meal today!")
