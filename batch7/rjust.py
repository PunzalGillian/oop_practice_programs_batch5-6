# Prog06. rjust() add space characters at the beginning of the string 
# to complete the number of characters specifies in function parameter.
# Create a program that do the same functionality without 
# using rjust() function.

input_string = input("Enter a string: ")
width = int(input("Enter the width: "))
fill_char = input("Enter the fill character: ")

if len(input_string) < width:
    fill_char = fill_char * (width - len(input_string))
else:
    fill_char = ''

print(fill_char + input_string)