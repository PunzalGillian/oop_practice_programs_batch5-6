# Prog02. removesuffix() remove the characters at the end of the string
# that matches the function parameter. Create a program that do 
# the same functionality without using removesuffix() function.

input_string = input("Enter a string: ")
suffix = input("Enter the suffix to remove: ")

if input_string.endswith(suffix) and suffix:
    print(input_string[:len(input_string) - len(suffix)])
else:
    print(input_string)