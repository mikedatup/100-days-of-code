#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
	 
#Write the rest of your code below this line 👇

import random

game = random.randint(0,1)
if game == 0:
    print("Heads")
elif game == 1:
    print("Tails")
