n=[7,11,23,56,78,68,87]
unique=[]
for i in n:
    if i not in unique:
        unique.append(i)

unique.sort()
print(unique[-2])