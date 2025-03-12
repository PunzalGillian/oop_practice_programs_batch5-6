# Prog05: Create a program that ask user to input a number
# Continue asking until the user input is invalid. 
# Display the average.

num_list = [] 

while True:
    try:
        num = float(input("Enter a number: "))
        num_list.append(num)
    except ValueError:
        average = sum(num_list) / len(num_list)
        print(f"Average is: {average}")
        break