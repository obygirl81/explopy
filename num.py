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
# To revceive the accurate calculation, we convert from one datatype to another. Below shows int and float. Float will have a decimal while int won't have a decimal. See below
#  int is integer ie whole  numbers like 4,3,2  while float is decimal like 1.2, 2.3, 4.5 etc so we use int and float function
print(int(first_num) + int(second_num))
print(float(first_num) + float(second_num))