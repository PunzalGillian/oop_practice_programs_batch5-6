# Prog01. rstrip() remove the space characters at the end of the string.
# Create a program that do the same functionality without 
# using rstrip() function.

input_string = input("Enter a string: ")
count = len(input_string) - 1

while count >= 0 and input_string[count] == ' ':
    count -= 1

print(input_string[:count + 1] + "|")
# The "|" is used to show the end of the string.

