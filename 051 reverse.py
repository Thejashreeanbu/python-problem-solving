n=int(input("Enter the three digit number: "))
first=n//100
second=(n//10)%10
last=n%10
result=last*100+second*10+first
print(result)