# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

BMI =  round(weight / height ** 2)

print(f" {weight} ÷ ({height} x {height}) = {BMI}")

if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI < 25:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI < 30:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI < 35:
    print(f"Your BMI is {BMI}, you are obese.")
elif BMI >= 35:
    print(f"Your BMI is {BMI}, you are clinically obese.")
else:
    print(f"Are you sure you entered weight and loss correctly?")