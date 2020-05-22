# Reviewing Lists and Arrays
# List are collection of items and ser set up using square brackets []. these items can be objects, strings, numbers etc
names = ['sara', 'John']
scores = []
scores.append(99) # Adds new item to the end
scores.append(100)
print(names)
print(scores)
print(scores[0])
print(scores[1])
# Arrays are also collection of items. To use an array, you have to create an array object and you get them by bringing them in from array library
from array  import array
scores = array('d')
scores.append(99)
scores.append(96)
print(scores)
print(scores[1])
print(scores[0])
# Common oeprations are shown below
names = ['Kevin', 'Flooki', 'Lucy']
print(len(names))  # will give the number  of items
names.insert(0, 'John') # this will insert before index
print(names)
names.sort()
print(names)