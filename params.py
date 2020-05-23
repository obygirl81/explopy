# Using multiple parameters in functions
def get_initial(name, force_uppercase=True): # added a boolean value so I dont have to pass in another in line 10. Although I can still leave value and code will stil run
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial

first_name = input('Enter your first name: ')
# first_name_initial = get_initial(first_name) # removed the previous False value
# using a named Notation
first_name_initial = get_initial(force_uppercase=False, name=first_name)

print('Your initial is: ' + first_name_initial)