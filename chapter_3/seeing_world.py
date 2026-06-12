places = ['rome', 'paris', 'japan', 'mexico', 'spain']

# Sorted
print(f"I'd love to visit {places}(OG)")
print(f"I'd love to visit {sorted(places)} (SORTED)\n")


print(f"{sorted(places, reverse=True)} (REVERSE SORTED)")
print(f"I'd love to visit {places}(OG)\n")

# Reverse
places.reverse()
print(f"{places} (REVERSED)") # Reversed

places.reverse()
print(f"{places} (RE-REVERSED) [OG]\n")

# Sort
places.sort()
print(f"{places} (SORT)")

places.sort(reverse=True)
print(f"{places} (REVERSE-ALPHA)")