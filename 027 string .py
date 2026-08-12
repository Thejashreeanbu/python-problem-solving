string="I LOVE PYTHON"
print("Accessing chara in string:",string[0])
print("string slicing:",string[3:7])
print("reverse string slicing:",string[::-1])
print("skip one chara using slicing:",string[::2])
print("string iteration")
for s in string:
    print(s)

print("slicing:",string[:0]+"Like")
print("concatenation:","Hello "+string[0:])
print("replace:",string.replace("I","We"))
hello = "Hello"
print("Formatting:", f"hi, {hello}")

