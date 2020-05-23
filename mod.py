# Using modules and packages
# Modules is a python file with fucntions, classes, and other components
# We use module to break down code into reuasble strucres and make code more readable
# Creating a module is shown below
def display(message, is_warning=False):
    if is_warning:
        print('Warning!!')
    print(message)
    
# Using a module. all we do is to import it. see below
# import module as namespace
import mod
mod.display('Not a warning')

# import all into current namespace
from mod import *
display('Not a warning')

#import specific items inti different namespace
from mod import display
display('Not a warning')
