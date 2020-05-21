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
# Using date functions  to control date formatting
print('Day: ' + str(current_date.day))
print('Month: ' + str(current_date.month))
print('Year: ' + str(current_date.year))
# Scenario where developer receives a date as a string. Dev will need to convert that date as a datetime object like below
birthday = input('What is your birthday (dd/mm/yyyy)? ')
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
print('Birthday: ' + str(birthday_date))
# Using date functions when you  have converted to a datetime object
one_day = timedelta(days=1)
birthday_eve = birthday_date - one_day
print('The day before birthday: ' + str(birthday_eve))
# Remember to add exception handling in your code in the case a user enters an invalid date
