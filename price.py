price = input('How much did you pay? ')

price = float(price)
if price >= 1.00:
    tax = .07
else:
    tax = 0
print('Your tax rate is ' + str(tax))

# comparing strings
hobby = input('What is your favorite hobby? ')
if hobby == 'tennis':
    print("yea! Me too!")
else:
    print("I'd like to try that sometime")