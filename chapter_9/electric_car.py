class Car:
    class Battery:
        def __init__(self, battery_size=40):
            self.battery_size = battery_size
        
        def describe_battery(self):
            print(f"This car has a {self.battery_size}-kWh battery")
        
        def getRange(self):
            if self.battery_size == 40:
                range = 150
            elif self.battery_size == 65:
                range = 225
            
            print(f"This car can go {range} miles on a full charge.")


    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    
    def get_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
        
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles
    
    def fill_gas_tank(self):
        print(f"Filling {self.get_name()} w/ GAS!")


class ElectricCar(Car):
    """Represents aspects of a car, specific to EV's"""

    def __init__(self, make, model, year):
        super().__init__(make,model,year)
        self.battery = super().Battery()

    
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        print("EV's don't take GAS!")


tesla = ElectricCar('tesla', 'model x', '2024')
print(tesla.get_name())
tesla.battery.describe_battery()
tesla.battery.getRange()