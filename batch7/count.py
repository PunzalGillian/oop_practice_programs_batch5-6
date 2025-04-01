# Prog08. count() return how many time the function parameter 
# appear in the string. Create a program that do the same
# functionality without using count() function.

input_string = input("Enter a string: ")
to_find = input("Enter a character to count: ")
count = 0
start_pos = 0 

while start_pos < len(input_string):
    pos = input_string.find(to_find, start_pos)
    if pos == -1:
        break
    count += 1
    start_pos = pos + 1

print(count)
