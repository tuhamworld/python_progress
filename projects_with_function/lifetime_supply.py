def calculate_supply(age,amount_per_day):
    max_age = 102
    age_difference = max_age - age
    amount_consumed_total = age_difference * amount_per_day
    result = amount_consumed_total * 365
    return f'You will need {int(result)} snacks to last you until the ripe old age of {max_age}'


print(calculate_supply(100, 2))
print(calculate_supply(52, 8))
print(calculate_supply(30, 11))