# Prog10. title() makes all first letter of each word in the string, 
# capital letter. And all other letter in small case. Create a program 
# that do the same functionality without using title() function.

input_string = input("Enter a string: ")
result = ""
words = input_string.split()

for word in words:
    for index, char in enumerate(word):
        if index == 0:
            result += char.upper()
        else:
            result += char.lower()
    result += " " 

print("Result:", result)