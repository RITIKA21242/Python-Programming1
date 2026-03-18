# Find key with maximum value in a dictionary

data = {
    'a':10,
    'b':9,
    'c':8,
    'd':7
}

max_key = max(data, key=data.get)
print("Key with maximum value: ", max_key)