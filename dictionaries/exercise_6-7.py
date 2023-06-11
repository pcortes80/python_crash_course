# Define dictionary
person_1 = {
    'first_name': 'isabel',
    'last_name': 'navia',
    'age': 40,
    'city': 'la serena',
    }
person_2 = {
    'first_name': 'pablo',
    'last_name': 'cortes',
    'age': 10,
    'city': 'la serena',
    }
person_3 = {
    'first_name': 'melissa',
    'last_name': 'cortes',
    'age': 4,
    'city': 'la serena',
    }

# Define a list of dictionaries called 'people':
people = [person_1, person_2, person_3]

# Loop through the people list
for person in people:
    print(person)
