# Prog10: Create a program that print all the numbers 
# starting from 0 to 100 except numbers ending in zero.

no_zero_ending_nums = []

for num in range(101):
    if num % 10 != 0:
        no_zero_ending_nums.append(num)

print(no_zero_ending_nums)