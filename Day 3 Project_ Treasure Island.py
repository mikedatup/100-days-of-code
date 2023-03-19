print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

print("You set foot into an island there are two pathways.")
question_1 = input("Would you like to go left or right? ")
question_1 = question_1.lower()
if question_1 == "left":
  print("You traversed the path and there's a small river in front of you.")
  question_2 = input("Would you like to swim or wait? ")  
  question_2 = question_2.lower()
  
  if question_2 == "wait":
    print("There's a small self guiding boat that let's you cross the river. on the other side theres a room. YOu enter and see three colored doors in from of you.")
    question_3 = input("What color door you would pick? Red, Blue or Yellow? ")
    question_3 = question_3.lower()
  
    if question_3 == "yellow":
      print("You win!")
    elif question_3 == "red":
      print("You are burned by fire. Game over")
    elif question_3 == "blue":
      print("You have been eaten by beasts!")
    else:
      print("Game over")
  else:
    print("You are attacked and murdered by trout. Game over.")
else:
  print("You fell into a hole! Game over.")

print("Would you like to play again?")