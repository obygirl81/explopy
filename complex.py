# Combining conditions with AND instead of nested if statements
# Combining operators allows you to handle complex rules in your code but you must test your code very carefully to avoid introducing errors
# A student makes honour roll if their average grade is >= 85 and their lowest grade is not below 70
gpa = float(input('What was your Grade Point Average? '))
# lowest_grade = input('What was your lowest grade? ')
# lowest_grade = float(lowest_grade)
lowest_grade = float(input('What was your lowest grade? '))

if gpa >= .85 and lowest_grade >= .70: # used the and statement here
    honour_roll = True
else:
    honour_roll = False
if honour_roll:
    print('You made honour roll!!')
