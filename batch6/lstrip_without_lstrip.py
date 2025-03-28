# Prog01. lstrip() remove the space characters at the beginning 
# of the string. Create a program that do the same functionality 
# without using lstrip() function.

char = 0
input_string = input("Enter a string: ")

while char < len(input_string) and input_string[char] == ' ':
    char += 1

print(input_string[char:])