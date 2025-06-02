import time

# Ask user which calculation to perform
choice3 = ""
while choice3 not in ['area', 'perimiter', 'volume']:
    choice3 = input("Would you like to work out area, perimeter or volume? ").lower()

time.sleep(0.5)

# Ask for dimensions
length = int(input("What is the length of the rectangle (in cm)? "))
time.sleep(0.5)
width = int(input("What is the width of the rectangle (in cm)? "))

# Function to calculate area
def area(length, width):
    shapeArea = length * width
    print("Area = length × width")
    time.sleep(1)
    print(f"Area = {length} × {width}")
    time.sleep(1)
    print("Area =", shapeArea, "cm²")

# Function to calculate perimeter
def perimeter():
    shapePerimeter = 2 * (length + width)
    print("Perimeter = 2 × (length + width)")
    time.sleep(1)
    print(f"Perimeter = 2 × ({length} + {width})")
    time.sleep(1)
    print("Perimeter =", shapePerimeter, "cm")

# Function to calculate volume
def volume(height):
    shapeVolume = length * width * height
    print("Volume = length × width × height")
    time.sleep(1)
    print(f"Volume = {length} × {width} × {height}")
    time.sleep(1)
    print("Volume =", shapeVolume, "cm³")

# Perform the appropriate calculation
if choice3 == "area":
    area(length, width)
elif choice3 == "perimeter":
    perimeter()
elif choice3 == "volume":
    height = int(input("What is the height of the rectangular prism (in cm)? "))
    time.sleep(0.5)
    volume(height)
else:
    print("Invalid choice. Please type 'area', 'perimeter' or 'volume'.")
