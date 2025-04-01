# Prog05. startswith() check if the string beginning part matches the 
# function parameter. Create a program that do the same functionality
# without using startswith() function.

input_string = input("Enter a string: ")
prefix = input("Enter the prefix to check: ")

print(input_string[:len(prefix)] == prefix if prefix else True)
