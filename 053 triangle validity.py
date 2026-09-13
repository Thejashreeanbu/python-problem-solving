a=int(input("Enter the side1: "))
b=int(input("Enter the side2: "))
c=int(input("Enter the side3: "))
if a+b>c and b+c>c and a+c>b:
    if a==b and b==c:
       print("Equilateral")
    elif a==b or b==c or a==c:
       print("Isoceles")
    else:
       print("Scalene")
else:
   print("Invalid triangle")