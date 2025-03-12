# Prog09: Create a program that print all the numbers starting 
# from 0 to 100 except numbers ending in zero or ending five.

no_num_ending_in_0_or_5 = []

for count in range(101):
    if count % 10 != 0 and count % 5 != 0:
        no_num_ending_in_0_or_5.append(count)

print(no_num_ending_in_0_or_5)
