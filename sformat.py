# several ways to custom  string formatting
first_name = input('Please  enter your first name: ')
last_name = input('Please  enter  your last name: ')
# output =  'Welcome ' + first_name + ' ' + last_name + ' ' + 'to my page!'
output =  'Welcome  {} {}' .format(first_name, last_name)
print(output)