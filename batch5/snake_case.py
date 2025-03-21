# Prog10: Create a program that ask the user to 
# input their fullname in incorrect casing. 
# Print the input in snake case.
# Example:
# Input: jUAn DEla CrUZ
# Output: juan_dela_cruz

while True:
    try: 
        name = str(input("Enter name: "))
        print(name.lower().replace(" ", "_"))
        break
    except ValueError:
        print("Invalid input")
