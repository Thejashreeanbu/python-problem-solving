n=int(input("Enter the value: "))
step=0
for i in range(1,n+1):
    if i%3 or i%5 == 0:
        step+=1
print("sum of multiple: ",step)
