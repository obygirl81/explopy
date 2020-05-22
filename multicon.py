# Checking multiple conditions to determine the correct action
country = input('What country do you live in? ')

if country.lower() == 'america':
    city = input('What city do you live in? ')

    if city == 'Denver' or city == 'Golden': # using or statement
        tax = 0.08
    elif city in('Aurora', 'Monument', 'Boulder'): # using in statement
        tax = 0.07
    elif city == 'Englewood':
        tax = 0.09
    else:
        tax = 0.20
else:
    tax = 0.18
print(tax)
