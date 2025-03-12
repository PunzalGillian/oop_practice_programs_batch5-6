# Prog02: Create a program that ask user to input a number, 
# Continue asking until the user input is invalid. 
# Display the number with the most number of duplicate.

num_list = []
duplicates = []

while True:
    try:
        num = int(input("Enter a number: "))
        num_list.append(num)
    except ValueError:
        if num_list.count(num) > 1:
            duplicates.append(num)
        break

max_duplicates = max(duplicates)
print("Number with most duplicates is: ", max_duplicates)

