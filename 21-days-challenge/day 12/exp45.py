# Write a Python function to find the maximum and minimum numbers from a sequence of numbers.  (Note: Do not use built-in functions.)

def find_max_min(arr):
    max_val = arr[0]
    min_val = arr[0]

    for i in arr:
        if i > max_val:
            max_val = i
        if i < min_val:
            min_val = i

    return max_val, min_val

numbers = [10, 20, 30, 40, 50]
print(find_max_min(numbers))