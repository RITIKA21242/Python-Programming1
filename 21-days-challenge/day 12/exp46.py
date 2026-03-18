# Write a Python function that takes a positive integer and returns the sum of the cube of all the positive integers smaller than the specified number.  

def sum_of_cubes(n):
    sum = 0
    for i in range(1, n):
        sum += i ** 3
    return sum

print(sum_of_cubes(5))