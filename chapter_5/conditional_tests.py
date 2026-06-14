player = 'Kobe'
print(player == 'Kobe') # True
print(player == 'kobe') # False
print(player == ' kobe ') # False
print(player.title() == 'Kobe') # True
print(player.title() == 'kobe')  # False
print(player.lower() == 'KOBE') # False
print(player.lower() == 'kobe') # True
print(player.upper() == 'KOBE') # True
print(player.upper().strip() == 'kobe') # False
print(player.upper().rstrip() == 'KOBE') # True