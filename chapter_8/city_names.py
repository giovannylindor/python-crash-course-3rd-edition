def city_country(name, country):
    string = f'{name.title()}, {country}'
    return string


print(city_country('Santiago', 'Chile'))
val = city_country(name='Boston', country='United States')
val_two = city_country('Chicago', country='USA')
print(val)
print(f"{val_two}")