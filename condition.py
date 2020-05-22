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