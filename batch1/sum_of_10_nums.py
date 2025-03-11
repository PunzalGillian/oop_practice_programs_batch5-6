# Prog07: Create a program that ask user to input 10 numbers. 
# Print the sum of all the numbers.

sum = 0 

for num in range(10):
    num = float(input("Enter a number: "))
    sum += num

print(sum)