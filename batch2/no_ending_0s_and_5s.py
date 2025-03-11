# Prog09: Create a program that print all the numbers starting 
# from 0 to 100 except numbers ending in zero or ending five.

# Count 0 to 100
# If number ends in 0 or 5, don't append in list
# Print the list

no_num_ending_in_0_or_5 = []

for count in range(101):
    if count % 10 != 0 and count % 5 != 0:
        no_num_ending_in_0_or_5.append(count)

print(no_num_ending_in_0_or_5)
