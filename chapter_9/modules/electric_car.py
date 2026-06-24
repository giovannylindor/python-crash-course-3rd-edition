from car import Car

class ElectricCar(Car):
    """Represents aspects of a car, specific to EV's"""

    def __init__(self, make, model, year):
        super().__init__(make,model,year)
        self.battery = super().Battery()

    
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        print("EV's don't take GAS!")