# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if size == "S":
    size_price = 15
elif size == "M":
    size_price = 20
elif size == "L":
    size_price = 25

if add_pepperoni == "Y":
    if size =="S":
        papperoni_price = 2
    else:
        papperoni_price = 3
if extra_cheese == "Y":
    extra_cheese_price = 1
final_bill = size_price + papperoni_price + extra_cheese_price

print(f"Your final bill is: ${final_bill}.")





        