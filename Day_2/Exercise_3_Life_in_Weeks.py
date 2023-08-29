# Instructions
# I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.

# https://waitbutwhy.com/2014/05/life-weeks.html

# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

# It will take your current age as the input and output a message with our time left in this format:

# You have x days, y weeks, and z months left.

# Where x, y and z are replaced with the actual calculated numbers.

# Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

# Example Input
# 56
# Example Output
# You have 12410 days, 1768 weeks, and 408 months left.

age = input("What is your current age?:\n")
living_age_goal = input("What is your living age goal?:\n")
days_in_year = 365
weeks_in_year = 52
months_in_year = 12

rest_of_life_in_days = (int(living_age_goal) *
                        days_in_year) - (int(age) * days_in_year)
rest_of_life_in_weeks = (int(living_age_goal) * weeks_in_year) - \
    (int(age) * weeks_in_year)
rest_of_life_in_months = (int(living_age_goal) * months_in_year) - \
    (int(age) * months_in_year)


print(
    f"You have {rest_of_life_in_days} days, {rest_of_life_in_weeks} weeks, and {rest_of_life_in_months} months left")
