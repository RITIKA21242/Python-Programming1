# Find GCD and LCM of two numbers

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return(a * b) // gcd(a, b)

x = int(input("enter first number: "))
y = int(input("enter second number: "))

print("GCD: ", gcd(x, y))
print("LCM: ", lcm(x, y))