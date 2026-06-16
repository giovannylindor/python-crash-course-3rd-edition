seating = input("How many people are in your group?\nPeople: ")
seating = int(seating)
MAX_SEATING = 8

if seating > MAX_SEATING:
    print("You'll have to wait for a table")
else:
    print(f"Table of {seating} is ready!")