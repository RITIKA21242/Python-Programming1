# Scan n values (0–3) and count occurrences

n = int(input("enter number of values: "))
count = [0, 0, 0, 0]

for _ in range(n):
    x=int(input())
    if 0 <= x <= 3: 
        count[x] += 1

for i in range(4):
    print(f"{i} occured {count[i]} times")