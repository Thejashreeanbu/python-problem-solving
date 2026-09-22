n = int(input("Enter the value: "))

largest = 0
count = 0

while n > 0:
    digit = n % 10
    n = n // 10

    if digit > largest:
        largest = digit
        count = 1

    elif digit == largest:
        count += 1

print("largest:", largest)
print("count:", count)