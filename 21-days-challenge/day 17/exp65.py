# Write a Python function to find the transpose of a given matrix.

def transpose_matrix(mat):
    rows = len(mat)
    cols = len(mat[0])
    t = []

    for j in range(cols):
        row = []
        for i in range(rows):
            row.append(mat[i][j])
        t.append(row)
    
    return t

a = [[1, 2],
     [3, 4],
     [5, 6]
     
     ]

print("\n transpose of a: ")
print(transpose_matrix(a))