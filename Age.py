# Days Alive Calculator

first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
age = int(input(f"Okay, {first_name} {last_name}, how old are you? "))

cal = age * 365
print(f"You have been alive for {cal} days.")

import time
time.sleep(2)

# Ask yes/no question
answer = input("Would you like to see how long in hours you have been alive for? (yes/no): ").strip().lower()

if answer == "yes":
    hours = cal * 24
    print(f"You have been alive for approximately {hours} hours!")
elif answer == "no":
    print("Okay, goodbye!")
else:
    print("Please answer with 'yes' or 'no'.")

                 