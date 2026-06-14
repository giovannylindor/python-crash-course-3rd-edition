text = 'sleep'
condition = True

my_list = [1, 2, 33]


if 33 in my_list:
    print(True)
else:
    condition = False
    print(False)


if text == 'sleep':
    condition = True
    print(True)
else:
    condition = False
    print(False)

if text.upper() == 'SLEEP':
    print(text.upper() == 'SLEEP')

if 'animals' not in my_list:
    print(True)