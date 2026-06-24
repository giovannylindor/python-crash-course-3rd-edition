from random import randint

class Die:

    def __init__(self, sides=6):
        if sides >= 6:
            self.sides = sides
    
    def roll_die(self):
        return randint(1, self.sides)


die_one = Die()

for i in range(10):
    die_one.roll_die()


die_two = Die(10)
die_three = Die(20)

print("\n10-sided die & 20-sided die: ")
for i in range(10):
    print(f"10-sided: {die_two.roll_die()}")

    print("\t\t20-sided: ")
    print(f"\t\t{die_three.roll_die()}")