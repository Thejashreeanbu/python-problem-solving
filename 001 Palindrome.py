palindrome=input("Enter the palindrome: ")
reverse_palindrome=palindrome[::-1]
if palindrome == reverse_palindrome:
    print("it is palindrome")
else:
    print("it is not a palindrome")