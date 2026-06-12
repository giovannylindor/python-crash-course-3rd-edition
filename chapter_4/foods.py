# Copying Lists 

my_foods = ['pizza', 'chicken', 'burgers']
fav_foods = my_foods[:]

print(fav_foods)

my_foods.append("French Fries")
print(my_foods)
print(fav_foods)

list_one = [1, 2, 3]
list_two = list_one # NOT A COPY 

list_two.append(4)
print(list_one)
print(list_two)


print("My fav foods are: ")
for food in my_foods:
    print(food)


print("\nBut if I HAD to pick: ")
for fav_food in fav_foods:
    print(fav_food)