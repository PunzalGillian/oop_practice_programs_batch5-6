# Prog04: Create a program that ask user to input a number,
# Continue asking until the user input is invalid. 
# Display the number from highest to lowest. Clue: sort() function

num_list = []

while True:
    try:
        num = int(input("Enter a number: "))
        num_list.append(num)
    except ValueError:
        num_list.sort(reverse=True)
        print(num_list)
        break
        