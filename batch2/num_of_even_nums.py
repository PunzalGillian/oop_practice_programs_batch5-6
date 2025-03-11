# Prog07: Create a program that ask user to input 10 numbers. 
# Print how many are even numbers.

even_counter = 0 

for numbers in range(10):
    num = float(input("Enter a number: "))
    if num % 2 == 0:
        even_counter += 1

print("The number of even numbers is:", even_counter)