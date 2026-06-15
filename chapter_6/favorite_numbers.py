fav_nums = {
    "Carl": [10, 3, 55, 45],
    "Josh": [17, 45],
    "Gio": [2,22, 222, 2_222_222],
    "Lucas": [3, 1028]
}

for name, num in fav_nums.items():
    print(f"\n{name.capitalize()}'s favorite numbers are: ")
    for n in num: 
        print(f"{n}")
