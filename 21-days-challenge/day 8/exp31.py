# Count occurrences of each alphabet (case-insensitive)

sentence = input("enter sentence: ")

words = sentence.split()

unique_words= set(words)
print("number of unique words: ", len(unique_words))