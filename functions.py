# Using functions is a way to write code efiiciently especially since we sometimes copy and paste our code
# printing timestamps to see how long sections take to run , copying and pasting 
import datetime

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
def print_time():
    print('task completed')
    print(datetime.datetime.now())
    print()
    
first_name = 'Ragnar'
print_time()

for x in range(0,10):
    print(x)
print_time()
    
