numbers=[1,2,3,2,4,5,6,1]
current=1
longest=1
for i in range(1,len(numbers)):
    if numbers[i]>numbers[i-1]:
        current+=1
    else:
        current=1
    if current>longest:
        longest=current
print("logest increasing streak length:",longest)
