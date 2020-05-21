# We need the current date and time when working with date so to get the current date and time, we use the datetime library
from  datetime import datetime, timedelta

current_date = datetime.now()
# the now function returns a datetime object see below
print('The date today is: ' +  str(current_date))
# Below are functions we can use with datetime objects to manipulate dates 
# the timedelta is used to define a period of time
today =  datetime.now()
print('Today is: ' + str(today))
one_day = timedelta(days=1)
yesterday = today - one_day
print('Yesterday was: ' + str(yesterday))
