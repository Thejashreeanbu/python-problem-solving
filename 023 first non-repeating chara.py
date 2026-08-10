def first_non_repeating(s):
    for char in s:
        if s.count(char) == 1:
            return char
    return None


text = "aabbcdde"

result = first_non_repeating(text)

if result:
    print(result)
else:
    print("No non-repeating character")