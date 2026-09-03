numbers=[10,5,8,20,15,20]
largest=float('-inf')#float('-inf') means negative infinity in Python.
second_largest=float('-inf')
for i in numbers:
    if i>largest:
        second_largest=largest
        largest=i
    elif i>second_largest and i!=largest:
        second_largest=i
print("second largest=",second_largest)

