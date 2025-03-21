# Prog04: Create a program that ask the user to input their fullname. Print the input in all lower case.
# Example:
# Input: Juan Dela Cruz
# Output: juan dela cruz

while True: 
    try:
        name = str(input("Enter your name: "))
        print(name.lower())
        break
    except ValueError:
        print("Invalid input")