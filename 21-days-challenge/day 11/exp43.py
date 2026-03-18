# Write a Python program to create a NumPy array and find the second largest element.

import numpy as np 
arr = np.array([10, 45, 23, 89, 67])

largest = arr[0]
second_largest = arr[0]

for i in arr:
    if i > largest: 
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
        second_largest = i

print("Second largest element: ", second_largest)