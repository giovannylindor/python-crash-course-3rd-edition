def build_sandwich(*items):
    print("\nBuilding a sandwich with the following: ")
    for item in items:
        print(f"- {item.title()}")

build_sandwich('bacon', 'lettuce', 'tomato')
build_sandwich('bacon', 'cheese', 'egg')
build_sandwich('bacon', 'cheese', 'sausage')