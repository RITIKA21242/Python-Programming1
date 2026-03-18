# Write a Python function to add two matrices.

def add_matrix(a, b):
    result = []

    for i in range(len(a)):
        row = []
        for j in range(len(a[0])):
            row.append(a[i][j] + b[i][j])
        result.append(row)
    
    return result

a = [[1, 2], 
     [3, 4],
     [5, 6]]

b = [[9, 8], 
     [7, 6],
     [5, 4]]

print("\n addition of a and b matrix is:")
print(add_matrix(a, b))