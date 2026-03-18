# Find maximum and minimum in NumPy array (no built-in max/min)

import numpy as np

arr = np.array([45, 12, 89, 23, 67])

max_val = arr[0]
min_val = arr[0]

for i in arr: 
    if i > max_val:
        max_val = i
    if i < min_val:
        min_val = i

print("Maximum : ", max_val)
print("Minimum : ", min_val)