 #Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
	 
#Write the rest of your code below this line 👇

import random
side = random.randint(0, 1)
if side == 1:
    print("Heads")
elif side == 0:
    print("Tails")
