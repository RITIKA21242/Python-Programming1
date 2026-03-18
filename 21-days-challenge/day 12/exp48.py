# Write a recursive function to print Fibonacci series upto n terms.

def fibonacci(n):
    if n <= 1:
        return n 
    return fibonacci(n-1) + fibonacci(n-2)

n = 7
for i in range(n):
    print(fibonacci(i), end="")