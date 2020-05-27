# using for loop and while loop
people = ['Mike', 'Susan', 'Logan']

for name in people:
    print(name)
    
for index in range(0,3):
    print(index)

people.append('Lucy')

print() # just putting an empty line
# for name in people:
#     print(name)
index = 0
while index < len(people):
    print(people[index])
    index = index + 1