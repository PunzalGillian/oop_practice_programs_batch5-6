# Prog09: Create a program that print all the
# even numbers starting from 0 to 100 (Use for loop).

even_nums = []

for count in range(101):
    if count % 2 == 0:
        even_nums.append(count)

print(even_nums)