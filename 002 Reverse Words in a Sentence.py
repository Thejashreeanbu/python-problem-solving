sentence = input("Enter a sentence: ")

words = sentence.split()

reverse_words = words[::-1]

result = " ".join(reverse_words) 

"""
#result = " ".join(words)  output-Python love I
#result = "-".join(words)  output-Python-love-I
"""
"""
" " → Join with spaces
"," → Join with commas
"-" → Join with hyphens
"" → Join without any separator
"""                                                           

print("Reversed Sentence:", result)