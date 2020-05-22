laura = {} # empty  dictionary or place holder
laura['first'] = 'Laura'
laura['last'] = 'Mongo'

Mya = {}  # empty list or place holder 
Mya['first'] = 'Mya'
Mya['last'] = 'Node'

people = []
people.append(laura)
people.append(Mya)
print(people)

people.append({
    'first':'Gloria', 'last': 'Young'
})
print(people)