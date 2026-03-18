# Check whether two matrices are Equal

def are_equal(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        return False
    
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] != b[i][j]:
                return False
    return True 

a = [[1,2], [3, 4]]
b = [[1,2], [3,4]]

print(are_equal(a,b))