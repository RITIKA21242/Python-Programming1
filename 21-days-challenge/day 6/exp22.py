 # Program to check whether a number is an Armstrong number

n= int(input("enter a number: "))
temp = n
sum = 0
digits = len(str(n))

while temp > 0:
    digit = temp % 10
    sum = sum + digit ** digits 
    temp = temp // 10

if sum == n:
    print("Armstrong number")
else: 
    print("Not an Armstrong number")