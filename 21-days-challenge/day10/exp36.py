# Create a NumPy array and find sum & average

import numpy as np

arr = ([10, 20, 30, 40, 50])

total = 0
for i in arr:
    total += i

avg = total / len(arr)

print("Sum: ", total)
print("Average: ", avg)


