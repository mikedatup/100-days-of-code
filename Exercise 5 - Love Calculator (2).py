# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1.lower()
name2.lower()

name = name1 + name2

t = name.count("t")
r = name.count("r")
u = name.count("u")
e1 = name.count("e")

score1 = t + r + u + e1

l = name.count("l")
o = name.count("o")
v = name.count("v")
e2 = name.count("e")

score2 = l + o + v + e2 

#print(score1)
#print(score2)

score = int(str(score1) + str(score2)) 

if score < 10 and score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score < 50 and score > 40:
    print(f"Your score is {score}, you are alright together.")
else:    
    print(f"Your score is {score}.")