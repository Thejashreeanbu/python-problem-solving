def reverse_string(s):
    reverse=""
    for i in range(s):
        reverse=i+reverse
    return reverse
reverse_string("HELLO")