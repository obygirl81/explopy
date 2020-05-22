#  for loops in python . The for and while
for name in ['Laura', 'Carey']:
    print(name)

print()    
for name in ['Orange', 'Apple', 'Grape']:
    print(name)
    
# When looping a number of times,use the built in range function.  Range will automatically create a list of numbers for you.
for index in range(0,2): # here 0 is the strting number while 2 is the number of items that we'll  get
    print(index)

#  while loop. Here you specify some confition. As long as some condition is met, you stay in the while loop. catch: must change the while loop condition to test as false at some point otherwise you will be stuck in while loop forever and end up getting a stack overflow!
places = ['Paris', 'London', 'Germany']
index = 0
while index < len(places):
    print(places[index])
    # Change the condition!
    index = index + 1
# this example may be better just using a while loop