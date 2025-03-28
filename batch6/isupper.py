# Prog04. isupper() check if all characters of the string is on upper
# case. Create a program that do the same functionality 
# without using isupper() function.

input_string = input("Enter a string: ")
is_upper = True
char = 0

while char < len(input_string):
    if 'A' <= input_string[char] <= 'Z':
        char += 1
    else:
        is_upper = False
        break

print(is_upper)