#Mobile phone costs
print("Hi, weclome to your monthly phone bill calculator.")

import time
time.sleep(1)

photos = int(input("How many photos do you take per month? "))

photos_price = photos * 0.35

time.sleep(1)

texts = int(input("Okay, how many texts do you send a month? "))

texts_price = texts * 0.10

time.sleep(1)

data = int(input("Okay, how much data (MB) do you use a month? "))

data_price = data * 0.05

bill = photos_price + texts_price + data_price

if bill > 10:
    print (f"It might be more cost effective to implement a contract as you are spending ${bill:.2f} on your phone bill")
    
else:
    print (f"You are currently spending ${bill:.2f} on your phone contract. This is cost effective as it is less than $10.")

time.sleep(1)
print("Harder part")

import math

time.sleep(1)

print("Data is charged at $2.50 per 500MB")
blocks = math.ceil(data/500)
data_price_hard = blocks * 2.50


bill_hard = photos_price + texts_price + data_price_hard

time.sleep(1)

if bill_hard > 10:
    print(f"(Harder Part) With the new data pricing, it might be more cost effective to implement a contract as you are spending ${bill_hard:.2f} on your phone bill")
else:
    print(f"(Harder Part) With the new data pricing, you are spending ${bill_hard:.2f} on your phone contract. This is cost effective as it is less than $10.")



