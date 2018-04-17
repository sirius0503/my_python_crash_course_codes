class Car():
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialize the attributes of car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    
    def get_descriptive_name(self):
        """Return a full descriptive name associated with car."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
        
        
    def update_odometer(self, mileage):
        """Update the mileage of the odometer."""
        if mileage >= self.odometer_reading:
            self.odometer = mileage
        else:
            print("You can't roll back an odometer!")
    
    
    def increment_odometer(self, miles):
        """Increments odometer reading by 'miles'. """
        self.odometer_reading += miles
        
        
class Battery():
    """A simple attempt to model a battery for an electric car."""
    
    def __init__(self,battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
        
        
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
        
        
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
        
        
    def upgrade_battery(self):
        """Upgrades battery size to '85' ,if not already set to '85'."""
        if self.battery_size == 70:
            self.battery_size = 85
        elif self.battery_size == 85:
            print("\nBattery size already is equal to 85.")
        
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()
        
        
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()


my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
            
