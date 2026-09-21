n=input("Enter the chara: ")
frequence={}
for i in n:
    if i in frequence:
        frequence[i]+=1
    else:
        frequence[i]=1
most_frequent=""
max=0
for i in frequence:
    if frequence[i]>max:
        max=frequence[i]
        most_frequent=i
print(most_frequent,"-",max)