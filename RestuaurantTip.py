#Secret password

secret_password = "BreenMachine"

while True:
    user_input = input("What is the password? ")
    if user_input == secret_password:
        print("Access Granted!")
        break
    else:
        print("Access denied, try again")
    
#Basic
        
import time

time.sleep(1)

print("Basic Module")

time.sleep(1)

total=(100*1.15)/2

print(f"${total:.2f}")

time.sleep(1)

#Harder

print("Harder module")

time.sleep(1)

num_people = int(input("How many people are there? "))

ask_percentage = int(input("Okay, what is the percentage(%) of the tip you want to leave? "))

tip = (ask_percentage / 100) * 100

total_price = 100 + tip

bill_per_person = total_price / num_people

print(f"Your tip should be ${tip:.2f}")

time.sleep(1)

print(f"Your new price is ${total_price:.2f}, where {num_people} people pay ${bill_per_person:.2f} each")

#Harder still

time.sleep(1)

print("Hardest Module")
time.sleep(1)

#Hardest

distance = float(input("How far (in miles) do you have to travel from the diner to your house? "))
taxi_price = distance * 0.45

print(f"You will pay ${taxi_price:.2f} to travel from the diner to your house")
time.sleep(1)

overall_price = bill_per_person + taxi_price

time.sleep(1)

print(f"You would have spent ${overall_price:.2f} for the day")