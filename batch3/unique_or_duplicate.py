# Prog03: Create a program that ask user to input a number, 
# Continue asking until the user input is invalid. Display "Unique" 
# After input when the inputted number don't have duplicate. 
# Display "Duplicate" after input when the inputted number have duplicate.

num_list = []

while True:
    try:
        num = int(input("Enter a number: "))
        num_list.append(num)
    except ValueError:
        for number in num_list:
            if num_list.count(number) == 1:
                print(f"{number} Unique")
            else:
                print(f"{number} Duplicate")
        break