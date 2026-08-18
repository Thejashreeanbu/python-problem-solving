def first_non_repeating(s):
    frequency={}
    for char in s:
       if char in frequency:
           frequency[char]+=1
       else:
           frequency[char]=1

    for char in s:
        if frequency[char]==1:
            return char

    return -1
print(first_non_repeating("swiss"))