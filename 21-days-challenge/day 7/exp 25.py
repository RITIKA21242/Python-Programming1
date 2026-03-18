# Program to check whether a number is Palindrome

n = int(input("enter a number: "))

temp = n
rev = 0
while temp > 0: 
    digit = temp % 10
    rev = rev * 10 + digit
    temp = temp //10

if rev ==n:
    print("Palindrome number")
else: 
    print("Not a Palindrome number")