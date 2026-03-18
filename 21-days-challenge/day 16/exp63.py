# Flatten a nested list (recursion)

def flatten_list(lst):
    flat = []
    for item in lst: 
        if isinstance(item, list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat

nested = [1, 2, [3, 4], [5, 6], 7, 8]
print(flatten_list(nested))