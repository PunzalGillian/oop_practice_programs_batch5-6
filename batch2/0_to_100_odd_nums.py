# Prog08: Create a program that print all the odd numbers 
# starting from 0 to 100. (Use while loop)

odd_nums = []
count = 0

while count != 100:
    if count % 2 != 0:
        odd_nums.append(count)
    count += 1

print(odd_nums)