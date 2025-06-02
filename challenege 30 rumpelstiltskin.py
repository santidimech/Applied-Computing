name = "Santi"

while True:
    user_input = input("What is the first name? ")
    if user_input == name:
        print("Access Granted!")
        break
    else:
        print("Access denied, try again")