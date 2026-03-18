# Find union, intersection, and difference of two sets

def set_operations(a, b):
    return a | b, a & b, a - b

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print(set_operations(s1, s2))