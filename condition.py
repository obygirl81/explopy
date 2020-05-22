# Taking different actions based on different conditions. See example below:
price = 1.05
# if price >= 1.00:
#     tax = .07
#     print(tax)
# # adding a default action using else
# else:
#     tax = 0
#     print(tax)    
# Another way of writing if else statement is shown below:
if price >= 1.00:
    tax = 0.07
else:
    tax = 0
print(tax)
# String comparision are case sensitive so be careful when comparing string.  See example below
country = 'AMERICA'
if country == 'america':
    print("You're an American") # used double quote because I have a signle quote inside the sentence
else:
    print("You're not from America") # used double quote because I have a signle quote inside the sentence