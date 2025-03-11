# Prog06: Create a program that ask user to input 10 numbers. 
# Print the result of the 1st number minus all of the remaining nums.

num_list = []

for numbers in range(10):
    num = float(input("Enter a number: "))
    num_list.append(num)

result = num_list[0] - sum(num_list[1:])
print("Num1 minus all of the remaining nums is:", result)