# Prog06. rjust() add space characters at the beginning of the string 
# to complete the number of characters specifies in function parameter.
# Create a program that do the same functionality without 
# using rjust() function.

# get user input
# get width and fill character
# check if the length of the character is less than the width
# if so, fill the string with the fill character
# else, fill the string with empty string
# print the string with the fill character at the start then the string

input_string = input("Enter a string: ")
width = int(input("Enter the width: "))
fill_char = input("Enter the fill character: ")

if len(input_string) < width:
    fill_char = fill_char * (width - len(input_string))
else:
    fill_char = ''

print(fill_char + input_string)