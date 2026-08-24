print("Give the string into small case")
n=input("Enter your string: ")
count=0
vowels=["a","e","i","o","u"]
for i in n:
    if i in vowels:
        count+=1
print("count vowels: ",count)