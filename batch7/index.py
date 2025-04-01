# Prog09. index() return the first location of the function parameter
# in the string. Create a program that do the same functionality without
# using index() function.

input_string = input("Enter a string: ")
search_string = input("Enter the character or string to search for: ")
index = -1

for char in range(len(input_string) - len(search_string) + 1):
    if input_string[char:char + len(search_string)] == search_string:
        index = char
        break

print(index)

