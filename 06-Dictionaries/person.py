person = {'first_name': 'mahmoud', 'last_name': 'seleem', 'Age': 30, 'city': 'cairo'}
print(f"The person first name is {person.get('first_name', 'Doesnot exist').title()}")
print(f"The person last name is {person['last_name'].title()}")
print(f"The person Age is {person['Age']}")
print(f"The pweson lives at {person['city'].title()}")