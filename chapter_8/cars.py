def make_car(manu, model, **info):
    info['Manufacturer'] = manu.title()
    info['Model'] = model.title()
    return info

car = make_car('subaru', 'outback', color='blue', tow_package=True) 
print(car)



