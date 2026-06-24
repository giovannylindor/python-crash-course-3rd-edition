from random import choice

rand_list = [2,3,4,5,6,3,7,3,1,9,'a','b','c','d','e']

# print("Any ticket matching these 4 letters wins a prize: ")

ticket = ''
tries = 0
#for i in range(4):
 #   rand_element = choice(rand_list)
  #  ticket += str(rand_element)

my_ticket = ['2b6c', '3e5g', 'a2d3', '5k92', '22a9', 'e677', '44ce']

loop = True
while loop:
    for i in range(4):
        rand_element = choice(rand_list)
        ticket += str(rand_element)
    
    tries += 1

    for winning_ticket in my_ticket:
        if ticket == winning_ticket:
            print(f"{winning_ticket} is the winning ticket!!"
                  f"\nIt took {tries} attempts to get it!")
            loop = False
            break
        
        
    ticket = ''
