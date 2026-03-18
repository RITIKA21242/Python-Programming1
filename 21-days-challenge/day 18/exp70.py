# Print all Strong Numbers between 1 and 1000

def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

for num in range(1, 1001):
    temp = num
    s = 0
    while temp > 0:
        digit = temp % 10
        s += factorial(digit)
        temp //= 10
    if s == num:
        print(num)