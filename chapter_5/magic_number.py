# Numerical Comparisons 
answer = 17
if answer != 100:
    print(f"{answer} isn't the correct answer!")

age = 15
print(age < 100) # True
print(age > 100) # False
print(age == 100) # False
print(age != 100) # True

# Multiple Connections 

num1 = 10
num2 = 11

print()
if num1 == 10 and num2 < 100:
    print(True)

print()
if num2 == 11 or num1 == 1_000_000:
    print(True)
