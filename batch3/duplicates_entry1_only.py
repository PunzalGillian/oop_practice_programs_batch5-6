# Prog02: Create a program that ask user to input 10 numbers. 
# Display all numbers. For numbers with duplicate
# Display only the first entry.

num_list = []
duplicate_entry1_only = []

for num_count in range(10):
    num = int(input("Enter a number: "))
    num_list.append(num)

for num in num_list:
    if num not in duplicate_entry1_only:
        duplicate_entry1_only.append(num)

print(duplicate_entry1_only)