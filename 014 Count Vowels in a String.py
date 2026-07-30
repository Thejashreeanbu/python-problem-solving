text = input("Enter a string: ")

count = 0
vowels = "aeiou"

for char in text.lower():
    if char in vowels:
        count += 1

print("Number of vowels:", count)