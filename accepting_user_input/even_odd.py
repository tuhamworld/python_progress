print('To get started, Please Enter your NAME below')

name = str(input())

print('Now Enter the NUMBER you\'d like to check')

#  Assigning numbers to a variable
num = int(input())

# Writing a conditional statement to check whether it is Odd or Even

if num % 2 == 0:
    print(f'This is an Even number, {name}!')
else:
    print(f'Oh No, {name}! This is an Odd Number')