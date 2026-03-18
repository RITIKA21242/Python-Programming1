# Write a Python function to subtract one matrix from another.

def subtract_matrix(a, b):
    result =[]

    for i in range(len(a)):
        row = []
        for j in range(len(a[0])):
            row.append(a[i][j] - b[i][j])
        result.append(row)
    return result

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]
     ]

b = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]
     ]

print("\n subtraction of a and b is:")
print(subtract_matrix(a, b))