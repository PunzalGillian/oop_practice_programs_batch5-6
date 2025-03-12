# Prog01: Create a program that ask user to input 10 numbers. 
# Display all numbers that don't have duplicate.

num_list = []
no_duplicates = []
unique_nums = []

for num_count in range(10):
    num = int(input("Enter a number: "))
    num_list.append(num)

for num in num_list:
    if num_list.count(num) == 1:
        unique_nums.append(num)

print(unique_nums)