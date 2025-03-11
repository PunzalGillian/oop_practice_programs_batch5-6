# Prog08: Create a program that ask user to input 10 numbers.
# Print how many are odd numbers.

odd_nums = []

for num in range(10):
    num = int(input("Enter a number: "))
    if num % 2 != 0:
        odd_nums.append(num)

num_of_odd_nums = len(odd_nums)
print(f"Number of odd numbers: {num_of_odd_nums}")
