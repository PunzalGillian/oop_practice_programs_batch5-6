# Prog03. upper() converts all characters of the string into upper 
# case. Create a program that do the same functionality without 
# using upper() function.

input_string = input("Enter a string: ")
result = ""
char = 0

while char < len(input_string):
    if 'a' <= input_string[char] <= 'z':
        # ascii value of 'a' is 97 and 'A' is 65
        result += chr(ord(input_string[char]) - 32)
    else: 
        result += input_string[char]
    char += 1

print(result)