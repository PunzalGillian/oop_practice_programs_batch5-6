# Prog02. removesuffix() remove the characters at the end of the string
# that matches the function parameter. Create a program that do 
# the same functionality without using removesuffix() function.

# get the string from the user and suffix to remove
# check if end of string matches the suffix
# if it does, remove the suffix and print the string
# if it does not, print the string as it is

input_string = input("Enter a string: ")
suffix = input("Enter the suffix to remove: ")

if input_string.endswith(suffix) and suffix:
    print(input_string[:len(input_string) - len(suffix)])
else:
    print(input_string)