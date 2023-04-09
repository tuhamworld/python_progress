# Using Python Shorthand

print('Please enter your Grade')
grade = int(input())

print('A') if grade > 79 else  print('B') if grade >= 70 and grade<=79 else print('C') if grade >=60 and grade<=69 else print('D') if grade >=50 and grade<=59 else print('E') if grade >=40 and grade<=49 else print('F')