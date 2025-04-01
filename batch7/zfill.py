# Prog07. zfill() add zero characters at the beginning of the string to 
# complete the number of characters specifies in function parameter. 
# Create a program that do the same functionality w
# without using zfill() function.

input_string = input("Enter a string: ")
num_characters = int(input("Enter the number of characters to fill: "))

if len(input_string) < num_characters:
    fill_zeros = '0' * (num_characters - len(input_string))
else:
    fill_zeros = ''

print(fill_zeros + input_string)