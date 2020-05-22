# Synatx errors, runtime errors, and logic errors are error types in python
#Below is an exmaple of a syntax error. Our code wont run at all with syntax error
# x = 20
# y = 102
# if x == print('Success')
# Runtime errors fail when run. Below is an example. It usually will give you alittle info on where to start trying to debug your code
# x = 22
# y = 0
# print(x / y)
# Logic error wont run at all. below is an example
# x = 102
# y = 22
# if x < y:
#     print(str(x) + ' is greater than ' + str(y))
# checking out try,except,finally 
x = 64
y = 0
    
print()
try:
    print(x / y)
except ZeroDivisionError as e:
    print('Not allowed to divide by zero')
else:
    print('Something else went wrong')
finally:
    print('This is my cleanup code')
print()