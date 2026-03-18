# Count occurrences of a substring (Left to Right)

s= input("enter a string : ")
sub = input("enter a substring: ")

count = 0
for i in range(len(s) - len(sub) + 1):
    if s[i:i+len(sub)] == sub: 
        count +=1

print(count)