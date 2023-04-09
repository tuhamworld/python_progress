# This program makes use of a function name called calculate_age and take in parameter to determine your present age

print(f'Enter your birth year')

birth_year = int(input())

print(f'Enter the current year')

current_year = int(input())

def calculate_age(birth_year, current_year):
    present_age = current_year - birth_year
    present_age_2 = present_age - 1
    return f'You are either {present_age} or {present_age_2}'

print(calculate_age(birth_year, current_year))

# print(calculate_age(2001, 2023))
# print(calculate_age(1970, 2025))
# print(calculate_age(2004, 2023))