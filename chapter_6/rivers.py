rivers = {
    "nile": 'egypt', 
    "amazon": 'brazil', 
    "yangtze": 'china'
}

# 1
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")

#2
print()
for river in rivers.keys():
    print(f"{river}")

# 3
print()
for country in rivers.values():
    print(f"{country}")