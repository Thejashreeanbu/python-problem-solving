n = int(input("Enter number: "))

decreasing = True
previous = n % 10
n //= 10

while n > 0:
    digit = n % 10

    if digit <= previous:
        decreasing = False
        break

    previous = digit
    n //= 10

print(decreasing)