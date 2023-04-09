#  This project creates an empty list, then make use of looping, conditional statements, and list append to yield Even Numbers


even_numbers_list = []

for n in range(4, 30):
    if n % 2 == 0:
        even_numbers_list.append(n)
        print(f'{even_numbers_list} \n')  # This prints the list step by step as it is being added.
    else:
        continue

print(f'Hence, the Final Result = {even_numbers_list} \n')    # This prints the final output