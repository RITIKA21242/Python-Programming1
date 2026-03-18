# Check if a list is a palindrome

def is_palindrome(lst):
    return lst == lst[::-1]

arr = list(map(int, input("enter elements: ").split()))

if is_palindrome(arr):
    print("Palindrome list")
else:
    print("Not a Palindrome list")