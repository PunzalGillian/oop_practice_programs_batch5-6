# Prog05: Create a program that ask user to input 2 numbers. 
# Print the remainder when the first number is divided by the second number.

num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))

remainder = num1 % num2
print(f"Remainder of two numbers is: {remainder:.0f}")
