guest_list = ['kobe bryant', 'jesus christ', 'yves saint laurent']

print(f"{guest_list[0].title()}, you're invited to my dinner!")
print(f"{guest_list[1].title()}, you're invited to my dinner!")
print(f"{guest_list[2].title()}, you're invited to my dinner!")
print()

# changing_guest_list
print(f"{guest_list.pop(-1).title()} can't make it to the dinner :(")
print()

guest_list.append('michael jackson')

print(f"{guest_list[0].title()}, you're invited to my dinner!")
print(f"{guest_list[1].title()}, you're invited to my dinner!")
print(f"{guest_list[2].title()}, you're invited to my dinner!")


# more_guests

print("It looks like I've found a bigger table!")

guest_list.insert(0, 'westside gunn')
guest_list.insert(1, 'shai-gilgeous alexander')
guest_list.append('prince')

print(f"{guest_list[0].title()}, you're invited to my dinner!")
print(f"{guest_list[1].title()}, you're invited to my dinner!")
print(f"{guest_list[2].title()}, you're invited to my dinner!")
print(f"{guest_list[3].title()}, you're invited to my dinner!")
print(f"{guest_list[4].title()}, you're invited to my dinner!")
print(f"{guest_list[5].title()}, you're invited to my dinner!")
print()


# shrinking_guest_list

print("uh oh! \nit looks like I can only invite 2 people to my dinner. yikes!")
print()

print(f"{guest_list.pop().title()}, sorry I can't invite you :( ")
print(f"{guest_list.pop().title()}, sorry I can't invite you :( ")
print(f"{guest_list.pop().title()}, sorry I can't invite you :( ")
print(f"{guest_list.pop().title()}, sorry I can't invite you :( ")
print()

print(f"{guest_list[0].title()}, you're still invited!")
print(f"{guest_list[1].title()}, you're still invited too!")

del guest_list[0]
del guest_list[0]
