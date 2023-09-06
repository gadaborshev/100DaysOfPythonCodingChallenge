# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
count_items = len(names)

random_index = random.randint(0, count_items - 1)

random_payer = names[random_index]

print(f"{random_payer} is going to buy the meal today!")