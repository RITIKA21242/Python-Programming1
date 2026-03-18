# Print numbers whose sum of digits is prime (1–100)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for num in range(1, 101):
    s = 0
    temp = num
    while temp > 0:
        s += temp % 10
        temp //= 10
        if is_prime(s):
            print(num)