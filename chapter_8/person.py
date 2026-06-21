def build_person(firstName, lastName, age=None): 
    person = {'first': firstName, 'last': lastName}
    
    if age:
        person['age'] = age

    return person


musician = build_person('jimi', 'hendrix', age=27)
print(musician)