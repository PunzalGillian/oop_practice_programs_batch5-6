# Prog09. capitalize() makes the first letter of the string, capital letter. 
# And all other letter in small case. Create a program that do the same 
# functionality without using capitalize() function.

input_string = input("Enter a string: ")
result = ""

for index, char in enumerate(input_string):
    if index == 0:
        result += char.upper()
    else:
        result += char.lower()
print("Result:", result)