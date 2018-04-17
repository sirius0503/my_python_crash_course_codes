class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make 
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    
    def get_descriptive_name(self):
        """Gives a descirption about the car."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
        
    
    def read_odometer(self):
        """Prints the mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self, mileage):
        """Updates the mileage of the car."""
        if mileage >= self.odometer_reading:
            self.odometer = mileage
        else:
            print("You can't roll back an odometer!")
            
    
    def increment_odometer(self,miles):
        """Increment odometer by 'miles' provided."""
        self.odometer_reading += miles
        
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric vehicle.
        """
        super().__init__(make, model, year)
        self.battery_size = 70
        
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("The car has a " + str(self.battery_size) + "-kWh battery.")
        
my_tesla = ElectricCar( 'tesla', 'model s', '2017')
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
        
        
        
