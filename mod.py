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

# The three codes above are doing the same thing, they are just written differently. Only different is how we call it. ther's no impact whatsoever
# Packages on the other hand is a published collection of modules. To install a package, must use pip. see examples below
# Install an individual package
# pip install colorama

# # Install from a list of packages
# pip install -r requirements.txt # a text file of all of the package that you'll be using

# requirements.text
# colorama

