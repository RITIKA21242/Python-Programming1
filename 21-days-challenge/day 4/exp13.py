# Check whether a number is divisible by both 3 and 5
num = int (input("enter a numer: "))
if num % 3 == 0 and num % 5 == 0: 
    print("multiple of both 3 and 5")
else: 
    print("not a multiple of 3 and 5")