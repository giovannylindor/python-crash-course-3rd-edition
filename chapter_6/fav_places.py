fav_places = {
    'mike': ['msg', 'pyramids', 'moda center'],
    'john': ['staples center', 'empire state'],
    'bron': ['american airlines arena', 'rodgers centre']
}


print("Here are some people and their favorite places: ")
for name, place in fav_places.items():
    print(f"\n{name.title()}'s favorite places to go to are: ")
    for p in place:
        print(f"{p.title()}")
