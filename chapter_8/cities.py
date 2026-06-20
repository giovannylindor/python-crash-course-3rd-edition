def describe_city(name, country='Spain'):
    print(f"{name.capitalize()} is in {country.title()}!")


describe_city('Sanjay', 'Italy')
describe_city(name='Mark', country='Germany')
describe_city(country='Mexico', name='Gio')