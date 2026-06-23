def city_country(name, country):
    string = f'{name.title()}, {country}'
    return string


def get_full_name(firstName, lastName, middleName=''):
    
    if middleName:
        fullName = f"{firstName} {middleName} {lastName}"
    else:
        fullName = f"{firstName} {lastName}"

    return fullName.title()


def show_messages(arr): 
    for message in arr:
        print(f"{message}")