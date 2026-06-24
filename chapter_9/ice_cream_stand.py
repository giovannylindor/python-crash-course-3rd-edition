class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()
        self.number_served = 0 
    

    def describe_restaurant(self):
        print(f"Our Restaurants name is {self.restaurant_name}"
              f"\nWe serve {self.cuisine_type}-Style Food!")
        
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")

    def set_servings(self, servings):
        if servings >= self.number_served:
            self.number_served = servings
        else:
            print("ERROR")
    
    def get_servings(self):
        return self.number_served
    
    def increment_servings(self, servings):
        self.number_served += servings


class IceCreamStand(Restaurant): 
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
    
    def print_flavors(self):
        print("Flavors: ")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")


flavors = ['peach', 'vanilla', 'chocolate', 'strawberry']

my_ice_cream_stand = IceCreamStand('Arbys', 'American', flavors)
my_ice_cream_stand.print_flavors()