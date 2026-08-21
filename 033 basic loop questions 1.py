
while True:
        print(" \n1. Factorial")
        print("2. count Prime Number")
        print("3. fibonacci")

        user=input("Enter the option: ")
        if user=="1":
            n=int(input("Enter the  number: "))
            fact=1
            for i in range(1,n+1):
                fact=fact*i
            print(fact)

        elif user=="2":
             n=int(input("Enter the number: "))
             count=0
             for i in range(2,n+1):
                    prime=True
                    for j in range(2,i):
                        if i%j==0:
                            prime=False
                            break
                    if prime:
                         count+=1
             print(count)

        elif user=="3":
             n=int(input("Enter number of terms: "))
             a=0
             b=1
             for i in range(n):
                  print(a)
                  c=a+b
                  a=b
                  b=c 
        else:
             print("Invalid option")   
        break
        

