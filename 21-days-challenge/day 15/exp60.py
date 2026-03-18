# Variable Length Argument

# Used when number of arguments is unknown.

def total(*numbers):
    s = 0
    for n in numbers:
        s += n
    return s

print(total(1, 2, 3, 4))