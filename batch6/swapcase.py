# Prog08. swapcase() reverse the casing of each of the character 
# of the string. Create a program that do the same functionality 
# without using swapcase() function.

# get the string from the user
# reverse the casing of each character by checking isupper() and islower()
# print the result

input_string = input("Enter a string: ")
result = ""

for char in input_string:
    if char.isupper():
        result += char.lower()
    elif char.islower():
        result += char.upper()
    else:
        result += char
        
print("Result:", result)
