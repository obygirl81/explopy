# We need the current date and time when working with date so to get the current date and time, we use the datetime library
from  datetime import datetime

current_date = datetime.now()
# the now function returns a datetime object see below
print('The date today is: ' +  str(current_date))
