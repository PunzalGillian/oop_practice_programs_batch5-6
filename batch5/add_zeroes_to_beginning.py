# Prog02: Create a program that ask the user to input a number (0-1000).
# Print the number in 6 digit format. 
# Add zeros at the beginning to complete the 6 digit.
# Example:
# Input: 143
# Output: 000143

while True: 
    try:
        num = int(input("Enter a number from (0-1000): "))
        if num < 0 or num > 1000:
            raise ValueError
        num = str(num)
        if len(num) == 4:
            print(f"00{num}")
        elif len(num) == 3:
            print(f"000{num}")
        elif len(num) == 2:
            print(f"0000{num}")
        elif len(num) == 1:
            print(f"00000{num}")
    except ValueError:
        print("Invalid input. Please enter a number from 0-1000.")

