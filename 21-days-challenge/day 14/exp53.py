# Write a Python function to find the maximum and minimum numbers from a sequence of numbers

def findmax_min(arr):
    max_val = arr[0]
    min_val = arr[0]

    for x in arr:
        if x > max_val:
            max_val = x
        if x < min_val:
            min_val = x

    return max_val, min_val

print(findmax_min([10, 6, 8, 90, 12, 56]))