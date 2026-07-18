sentence = input("Enter a sentence: ")

words = sentence.split()

reverse_words = words[::-1]

result = " ".join(reverse_words)

print("Reversed Sentence:", result)