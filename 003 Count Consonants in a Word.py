word = input("Enter a word: ").lower()

vowels = ["a", "e", "i", "o", "u"]
count = 0

for letter in word:
    if letter.isalpha() and letter not in vowels:
        count += 1

print("Number of consonants:", count)