laura = {} # empty  dictionary or place holder. Can use to create an object
laura['first'] = 'Laura'
laura['last'] = 'Mongo'

Mya = {} 
Mya['first'] = 'Mya'
Mya['last'] = 'Node'

people = []  # empty list or place holder . Can use list to add multiple things
people.append(laura)
people.append(Mya)
print(people)

people.append({
    'first':'Gloria', 'last': 'Young'
})
print(people)