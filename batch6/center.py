# Prog07. center() add space characters at the beginning and at the end
# of the string to print the string at the center. Create a program
# that do the same functionality without using center() function.

# get string input
# center string add space at beginning and end
# print string

input_string = input("Enter a string: ")
width = int(input("Enter the width: "))

if len(input_string) < width:
    space_char = " " * ((width - len(input_string) // 2))
    fill_char = "*" * ((width - len(input_string) // 2))
else:
    fill_char = " "

print(space_char + input_string + space_char)
print(fill_char + input_string + fill_char)
