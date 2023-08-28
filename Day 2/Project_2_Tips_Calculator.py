#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")


total_bill = input("What was the total bill?\n$")
tip_percent = input("How much tip would you like to give? 10, 12 or 15?\n")
count_of_guests = input("How many people to split the bill?\n")

total_bill = float(total_bill)
tip_percent = float(tip_percent)
count_of_guests = int(count_of_guests)
result_bill_for_each_person = total_bill / \
    count_of_guests * (1 + tip_percent / 100)

message = f"Each person should pay: ${round(result_bill_for_each_person, 2)}"
print(message)