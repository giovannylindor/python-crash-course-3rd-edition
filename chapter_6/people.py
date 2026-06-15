person = {
    "firstName": "John",
    "lastName": "Doe",
    "Age": 22,
    "City": "Brooklyn"
}

person_2 = {
    'firstName': 'Thadd',
    'lastName': 'Allonce',
    'Age': 22,
    'City': 'Brooklyn'
}

person_3 = {
    'firstName': 'Jabary',
    'lastName': 'Nelson',
    'Age': 19,
    'City': 'Amityville'
}

# loop through list
people = [person, person_2, person_3]


print("All People: ")
for person in people: 
    print(f"\nFirst Name: {person['firstName']}")
    print(f"Last Name: {person['lastName']}")
    print(f"Age: {person['Age']}")
    print(f"City: {person['City']}")
    
    if person['firstName'] == 'Thadd':
        print("Thadd is 6'3.5")
    elif person['firstName'] == 'Jabary':
        print("Jabary is an HVAC Technician")
    elif person['firstName'] == 'John':
        print("IDK anything about John :( ")