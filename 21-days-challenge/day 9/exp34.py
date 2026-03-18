# Create a tuple and find the average

n =int(input("enter number of elements: "))
t = ()

for _ in range(n):
    t += (int(input()),)

avg = sum(t) / n
print("Average : ", avg)