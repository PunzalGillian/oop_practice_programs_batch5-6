# Prog07: Create a program that ask the user to 
# input a complete statement. 
# Print the number of words in the input.
# Example:
# Input: We will weather the weather whatever 
# the weather whether we like it or not
# Output: 14

while True:
    try:
        statement = str(input("Enter a statement: "))
        num_of_words = len(statement.split())
        print(num_of_words)
        break
    except ValueError:
        print("Invalid input")