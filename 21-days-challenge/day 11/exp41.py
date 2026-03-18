# Write a Python program to create a NumPy array and count how many elements are even and odd.

import numpy as np
arr=([10, 15, 20, 25, 30, 35])

even_count=0
odd_count=0

for i in arr:
    if i % 2 == 0:
        even_count += 1
    else: 
        odd_count += 1

print("Even elements: ", even_count)
print("Odd elements: ", odd_count)