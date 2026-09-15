n=int(input("Enter your digit: "))
count={}
while n>0:
    digit=n%10
    if digit in count:
        count[digit]+=1
    else:
        count[digit]=1
    n=n//10
for digit in count:
        print(digit,"-",count[digit])
