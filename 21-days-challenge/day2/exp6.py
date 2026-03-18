s= input("enter a string:")
vowel=0
for ch in s: 
    if ch in 'aeiouAEIOU':
        vowel+=1
print("number of vowels in string is:",vowel)