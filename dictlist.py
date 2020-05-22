laura = {} # empty  dictionary or place holder. Can use to create an object on the fly
laura['first'] = 'Laura'
laura['last'] = 'Mongo'

mya = {} 
mya['first'] = 'Mya'
mya['last'] = 'Node'

people = []  # empty list or place holder . Can use list to store multiple things including adding other dictionaries
people.append(laura)
people.append(mya)
print(people)

people.append({
    'first':'Gloria', 'last': 'Young'
})
print(people)