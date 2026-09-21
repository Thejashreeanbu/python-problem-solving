n=input("Enter the chara: ")
frequence={}
for i in n:
    if i in frequence:
        frequence[i]+=1
    else:
        frequence[i]=1
for i in frequence:
    print(i,"-",frequence[i])