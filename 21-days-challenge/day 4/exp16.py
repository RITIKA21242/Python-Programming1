# Find the greatest among three numbers (no two are same)

a = int(input("enter first number: " ))
b= int(input("enter second number: " ))
c = int(input("enter third number: " ))

if a>b and a>c:
    print("greater number is : ", a)
elif b>a and b>c:
    print("greater number is: ", b)
else:
    print("greater number is : ", c)