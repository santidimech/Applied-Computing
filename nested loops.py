#Input part
import time
number = int(input("Enter the number you want the times table for: "))

#Displays the time tables
print(f"\n{number} Times Table")
print("-" * 20)

time.sleep (1)
for j in range(1, 13):
    print(f"{number} x {j} = {number * j}")
