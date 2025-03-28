# Prog02. removeprefix() remove the characters at the
# beginning of the string that matches the function parameter.
# Create a program that do the same functionality
# without using removeprefix() function.

input_string = input("Enter a string: ")
prefix = input("Enter the prefix to remove: ")

if input_string.startswith(prefix) and prefix:
    print(input_string[len(prefix):])   
else:
    print(input_string)