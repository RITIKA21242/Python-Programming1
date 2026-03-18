# Set operations on fruits

s1 = set(input("enter fruits for set 1: ").split())
s2 = set(input("enter fruits for set 2: ").split())

print("fruits in both s1 and s2:", s1 & s2)
print("fruits only in s1:", s1-s2)
print("count of all fruits:", len(s1 | s2))