# Prog05. endswith() check if the string end part matches the function
# parameter. Create a program that do the same functionality 
# without using endswith() function.

input_string = input("Enter a string: ")
suffix = input("Enter the suffix to check: ")

print(input_string[-len(suffix):] == suffix if suffix else True)
