# Prog03. lower() converts all characters of the string into lower case.
# Create a program that do the same functionality without 
# using lower() function.

input_string = input("Enter a string: ")
result = ""
char = 0 

while char < len(input_string):
    if 'A' <= input_string[char] <= 'Z':
        # ascii value of 'A' is 65 and 'a' is 97
        result += chr(ord(input_string[char]) + 32)
    else:
        result += input_string[char]
    char += 1

print(result)