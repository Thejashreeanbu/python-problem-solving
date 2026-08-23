while True:
    print("/n 1.Armstrong Number")
    print("2.GCD")
    print("3.Reverse Number")

    user=int(input("Enter your option: "))

    if user==1:
        n=int(input("Enter the value: "))
        original=n
        total=0
        while n>0:
            digit=n%10
            total=total+digit**3
            n=n//10
        print(total)
        if total==original:
                print("It is armstrong number")
        else:
             print("Not a armstrong number")

    elif user==2:
         a=int(input("Enter the value a: "))
         b=int(input("Enter the value b: "))
         while b!=0:
              a,b=b,a%b
         print("GCD",a)

    elif user==3:
         a=int(input("Enter the number: "))
         total=0
         while a>0:
              digit=a%10
              total=total*10+digit
              a=a//10
         print("reverse number: ",total)

    else:
         print("Invalid option")


    break
            
            