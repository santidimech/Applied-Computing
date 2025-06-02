salesAmount=float(input("Enter the amount of money spent "))
if salesAmount > 20:
    print("You qualify for a 3 pound voucher")
elif salesAmount > 10:
    print("You qualify for a 1 pound voucher")
else:
    print("You dont qualify for a voucher")