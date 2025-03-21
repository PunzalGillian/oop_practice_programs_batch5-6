# Prog09: Create a program that ask the user to
# input their fullname in incorrect casing.
# Print the input in pascal case.
# Example:
# Input: jUAn DEla CrUZ
# Output: JuanDelaCruz
while True:
    try:
        name= str(input("Enter your name: "))
        print(name.title().replace(" ", ""))
        break
    except ValueError:
        print("Invalid input")