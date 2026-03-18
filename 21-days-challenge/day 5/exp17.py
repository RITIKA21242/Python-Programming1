# Check whether a quadratic equation has real or imaginary roots (and display them)

import math

a=float(input("enter a: "))
b= float(input("enterb:"))
c = float(input("enter c: "))

d = b*b - 4*a*c

if d>0: 
    r1=(-b +math.sqrt(d)) / (2*a)
    r2= (-b - math.sqrt(d)) / (2 * a)
    print("real and distinct roots:", r1, r2)
elif d==0:
    r=-b/(2*a)
    print("real and equal roots", r)
else:
    real = -b / (2*a)
    imag= math.sqrt(-d) / (2*a)
    print("imaginary roots:", real, "+/-", imag, "i")

