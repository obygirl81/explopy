first_num  = 5
second_num =  8
print(first_num + second_num)
# all Operation use the same math symbol known  to all except Exponent. Exponent uses **
print(first_num - second_num)
print(first_num * second_num)
print(first_num  /  second_num)
print(first_num **  second_num)
# Python gets confused when strings are combined  with numbers so we have to do type conversion. Example below shows the conversion of a number to a string
days_in_feb = 28
print(str(days_in_feb) + ' days in February')
# Numbers stored as strings are treated as strings and when added together, the first value is concatenated to the second value. See below:
first_num = '8'
second_num = '10'
print(first_num + second_num)
#  Input number always returns strings
first_num = input('Enter your first number ')
second_num = input('Enter your second number ')
print(first_num + second_num)