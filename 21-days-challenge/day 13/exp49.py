# Write a function to display characters at even index positions.

def even_index_chars(s):
    for i in range(0, len(s), 2):
        print(s[i], end = "")

even_index_chars("python")