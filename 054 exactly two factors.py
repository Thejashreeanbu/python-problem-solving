n = int(input("Enter N: "))

count = 0

for num in range(2, n + 1):

    factors = 0

    for i in range(1, num + 1):
        if num % i == 0:
            factors += 1

    if factors == 2:
        count += 1

print(count)