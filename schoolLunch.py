import time
print("Your Name's calorie counter")
calories = int(input("How many calories have you eaten today?"))
s=2000-calories
print("You can eat", s, "more calories today")
time.sleep(2)
money = int(input("How much money ($) do you have for lunch today?"))
food = int(input("How much is the item you want to buy?"))
r= money-food
print ("You will have $",r,"left after the purchase")