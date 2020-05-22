# Checking multiple conditions to determine the correct action
city = input('What city do you live in? ')
tax = 0

if city == 'Denver' or city == 'Golden': # using or statement
    tax = 0.08
elif city in('Aurora', 'Monument', 'Boulder'):
    tax = 0.07
elif city == 'Englewood':
    tax = 0.09
else:
    tax = 0.20
print(tax)