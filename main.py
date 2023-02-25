#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

before_tip = float((input("How much is the bill? ")))
after_tip = before_tip * 1.12
people = int((input("How many people in the party? ")))
per_person = after_tip / people
print("Each person should pay " + str(per_person))

