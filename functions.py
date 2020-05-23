# Using functions is a way to write code efiiciently especially since we sometimes copy and paste our code
# printing timestamps to see how long sections take to run , copying and pasting 
from datetime import datetime

# first_name = 'Gloria'
# print('task completed')
# print(datetime.datetime.now())
# print()

# for x in range(0,10):
#     print(x)
# print('task completed')
# print(datetime.datetime.now())
# print()

# Using functions - its better to write a function and call it when you need it rather than continous copying and pasting code. See example below:
# Print the current time
# def print_time():
#     print('task completed')
#     # print(datetime.datetime.now())
#     print(datetime.now()) # a better way of rewriting the code i have on line 20 since I adjusted teh statement on line 3
#     print()
    
# first_name = 'Ragnar'
# print_time()

# for x in range(0,10):
#     print(x)
# print_time()
    
# Passing parameter in functions
# Printing current time and task name
def print_time(task_name):
    print(task_name)
    print(datetime.now())
    print()
    
first_name = 'Yolanda'
print_time('first name as assigned')

for x in range(0,10):
    print(x)
print_time('loop completed')

# Working with a function that returns a value
# def get_initial(name):
#     initial = name[0:1]
#     return initial

# first_name = input('Enter your first name: ')
# first_name_initial = get_initial(first_name)

# last_name = input('Enter your last name: ')
# last_name_initial = get_initial(last_name)

# print('Your initials are ' + first_name_initial + last_name_initial)

# Showing same function above but with less code below:
def get_initial(name):
    initial = name[0:1].upper()
    return initial

first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')

print('Your initials are: ' \
    + get_initial(first_name) \
    + get_initial(last_name))