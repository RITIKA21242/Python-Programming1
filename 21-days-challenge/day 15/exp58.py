# Lambda function to return (max, min) from a list

# Sample input: [10, 6, 8, 90, 12, 56]
# Sample output: (90, 6)

max_min = lambda lst: (
    (lambda mx, mn: (mx, mn))(
        (lambda: [x for x in lst if all(x >= y for y in lst)][0])(),
        (lambda: [x for x in lst if all(x <= y for y in lst)][0])()
    )
)

print(max_min([10, 6, 8, 90, 12, 56]))
