# Count Even and Odd Elements in a Matrix

def count_even_odd(mat):
    even = 0
    odd = 0

    for row in mat:
        for val in row:
            if val % 2 == 0:
                even += 1
            else:
                odd += 1
    
    return even, odd

a = [[1, 2, 3],
     [4, 5, 6]
     ]

print(count_even_odd(a))