# Prog03: Create a program that ask the user to input their fullname. Print the input in all capital letter.
# Example:
# Input: Juan Dela Cruz
# Output: JUAN DELA CRUZ

while True:
    try: 
        name = str(input("Enter your full name: "))
        print(name.upper())
        break
    except ValueError: 
        print("Invalid input")