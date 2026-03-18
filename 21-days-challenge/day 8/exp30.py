# Count occurrences of each alphabet (case-insensitive)

s= input("enter a string: ").upper()
d={}

for ch in s:
    if ch.isalpha():
        d[ch] = d.get(ch, 0) + 1

for k in sorted(d):
    print(d[k], k, sep="")