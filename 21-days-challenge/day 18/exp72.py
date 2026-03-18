# Count vowels, consonants, digits, and spaces in a string

s = input("enter a string: ")

vowels = consonants = digits = spaces = 0

for ch in s:
    if ch.lower()in 'aeiou':
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch == '':
        spaces += 1

print("vowel:", vowels)
print("consonants:", consonants)
print("digits:", digits)
print("spaces:", spaces)