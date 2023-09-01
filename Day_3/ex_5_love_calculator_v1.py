# program version 1

# 🚨 Don't change the code below 👇
# print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1_lower_case = name1.lower()
name2_lower_case = name2.lower()

score = int(str(int(name1_lower_case.count('t')) + \
int(name1_lower_case.count('r')) + \
int(name1_lower_case.count('u')) + \
int(name1_lower_case.count('e')) + \
int(name2_lower_case.count('t')) + \
int(name2_lower_case.count('r')) + \
int(name2_lower_case.count('u')) + \
int(name2_lower_case.count('e'))) + \

str(int(name1_lower_case.count('l')) + \
int(name1_lower_case.count('o')) + \
int(name1_lower_case.count('v')) + \
int(name1_lower_case.count('e')) + \
int(name2_lower_case.count('l')) + \
int(name2_lower_case.count('o')) + \
int(name2_lower_case.count('v')) + \
int(name2_lower_case.count('e'))))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
if score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")