# Prog08: Create a program that ask the user to input their fullname. 
# Print the number of characters in the input.
# Example:
# Input: Juan Dela Cruz
# Output: 14

while True: 
    try:
        name = str(input("Enter your name: "))
        print(len(name))
        break
    except ValueError:
        print("Invalid input")