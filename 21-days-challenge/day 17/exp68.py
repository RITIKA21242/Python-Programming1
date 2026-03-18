# Write a Python function to multiply two matrices.

def multiply_matrix(a, b):
    result= []

    for i in range(len(a)):
        row =[]
        for j in range(len(a[0])):
            s = 0
            for k in range(len(b)):
                s += a[i][k] * b [k][j]
            row.append(s)
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

print("\n multiplication of a and b matrices: ")
print(multiply_matrix(a, b))