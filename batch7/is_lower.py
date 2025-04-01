# Prog04. islower() check if all characters of the string is 
# on lower case. Create a program that do the same 
# functionality without using islower() function.

input_string = input("Enter a string: ")
is_lower = True
char = 0

while char < len(input_string):
    if 'a' <= input_string[char] <= 'z':
        char += 1
    else:
        is_lower = False
        break

print(is_lower)