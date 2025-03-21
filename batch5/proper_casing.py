# Prog05: Create a program that ask the user to input their fullname in incorrect casing.
# Print the input in proper casing.
# Example:
# Input: jUAn DEla CrUZ
# Output: Juan Dela Cruz

while True:
    try:
        name = str(input("Enter your name: "))
        print(name.title())
        break
    except ValueError:
        print("Invalid input")