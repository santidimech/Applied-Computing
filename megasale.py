#Mega Sale
spent=int(input("How much have you spent today? "))

if spent>20:
    print("Congratualtions! You qualify for a £3 voucher.")
    
elif spent>10:
    print("Congratualtions! You qualify for a £1 voucher.")
else:
    print("You do not qualify for a voucher as you did not spend enough.")
