# Prog08. count() return how many time the function parameter 
# appear in the string. Create a program that do the same
# functionality without using count() function.

# get user string input
# get user character input
# initialize a counter variable to 0
# loop through each character in the string 
# and check if it matches the character input
# if it matches, increment the counter variable
# print the counter variable

input_string = input("Enter a string: ")
to_find = input("Enter a character to count: ")
count = 0

for char in input_string:
    if char == to_find:
        count += 1

print(count)