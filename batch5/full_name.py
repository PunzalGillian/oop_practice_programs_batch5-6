# Prog01: Create a program that ask the user to input their fullname 
# with several space characters at the beginning.
# Print the input without the spaces in the beginning.
# Example:
# Input:         Juan Dela Cruz
# Output: Juan Dela Cruz

name = str(input("Enter your full name with spaces at the beginning: "))
print(name.lstrip())