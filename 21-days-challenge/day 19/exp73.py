# Check whether a matrix is Symmetric

def is_symmetric(mat):
    rows = len(mat)
    cols = len(mat[0])

    if rows != cols:
        return False
    
    for i in range(rows):
        for j in range(cols):
            if mat[i][j] != mat[j][i]:
                return False
    return True 

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]
     ]

print(is_symmetric(a))