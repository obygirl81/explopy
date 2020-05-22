# Checking multiple conditions to determine the correct action
city = input('What city do you live in? ')
tax = 0

if city == 'Denver':
    tax = 0.08
elif city == 'Aurora':
    tax = 0.07
elif city == 'Englewood':
    tax = 0.09
print(tax)