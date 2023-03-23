rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

rps = [rock, paper, scissors]
pc_pre = int(len(rps)) - 1
pc_num = random.randint(0,pc_pre)
pc_plays = rps[pc_num]

P1_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
P1_plays = rps[P1_input]

print(P1_plays)
print("Computer chose:")
print(pc_plays)

if pc_plays == P1_plays:
  print("It's a draw")
if pc_num + 1 == P1_input:
  print("You win!")
if P1_input + 1 == pc_num:
  print("You lose!")
if pc_num + 2 == P1_input:
  print("You lose!")
if P1_input + 2 == pc_num:
  print("You win!")
