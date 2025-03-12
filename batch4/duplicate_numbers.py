# Prog01: Create a program that ask user to input 10 numbers. 
# Display all numbers that have duplicate.

num_list = []
duplicates = []
numbers_with_duplicates = []

for num in range(10):
    num = float(input("Enter a number: "))
    num_list.append(num)

for num in num_list:
    if num not in duplicates and num_list.count(num) > 1:
        numbers_with_duplicates.append(num)
    if num_list.count(num) > 1:
        duplicates.append(num)

print(sorted(duplicates))
print(numbers_with_duplicates)

