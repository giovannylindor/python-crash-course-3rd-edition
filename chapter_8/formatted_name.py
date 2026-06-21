def get_full_name(firstName, lastName, middleName=''):
    
    if middleName:
        fullName = f"{firstName} {middleName} {lastName}"
    else:
        fullName = f"{firstName} {lastName}"

    return fullName.title()

name = get_full_name('jimi', 'hendrix')
print(name)

name = get_full_name('wardell','curry', 'stephen')
print(name)