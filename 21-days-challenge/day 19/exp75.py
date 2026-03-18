# Find Maximum and Minimum element in a Matrix

def max_min_matrix(mat):
    max_val = mat[0][0]
    min_val = mat[0][0]

    for row in mat:
        for val in row:
            if val > max_val:
                max_val = val
            if val < min_val:
                min_val = val
    return max_val, min_val

a = [[3, 5, 1],
     [9, 2, 8]
     ]

print(max_min_matrix(a))