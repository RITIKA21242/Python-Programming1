# Write a program to extract all digits from a string.

def extract_digits(s):
    digits = ""
    for ch in s:
        if ch.isdigit():
            digits += ch
    return digits

print(extract_digits("abcdef12345jbibj2079"))