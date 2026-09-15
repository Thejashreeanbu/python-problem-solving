n=int(input("Enter the digits: "))
previous=n%10
n//=10
result=True
while n>=10:
    digit=n%10
    if digit>=previous:
        result=False
        break
    previous=digit
    n=n//10
print(result)