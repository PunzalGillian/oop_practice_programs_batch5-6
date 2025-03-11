# Prog04: Create a program that ask user to input 2 numbers. 
# Print the quotient of the two numbers without the decimal point.

num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))

quotient = num1 // num2
print(f"Quotient of two numbers is: {quotient:.0f}")