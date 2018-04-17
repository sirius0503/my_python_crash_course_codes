class Restaurent():
    """Typical information on a specific restaurent."""
    
    def __init__(self, restaurent_name, cuisine_type ):
        """Initialize name and cuisine attributes."""
        self.name = restaurent_name
        self.cuisine = cuisine_type
        self.number_served = 0
    
    def describe_restaurent(self):
        """Gives name & cuisine info about the restaurent."""
        print("\nThe restaurent is named: " + self.name.title())
        print("The restaurent serves: " + self.cuisine.title() + " cuisine.")
        
    def open_restaurent(self):
        """Message indicating that the restaurent is open."""
        print("\nThe restaurent is currently open!")
        
    def set_number_served(self, customer_served):
        """Method sets the number of customer served."""
        self.number_served = customer_served
        
    def increment_number_served(self, increase):
        """Increments the number_served attribute by increase."""
        self.number_served += increase


class IceCreamStand(Restaurent):
    """
    A class which inherits from the Restaurent class and represents
    ice cream stands
    """
    
    
    def __init__(self, restaurent_name, cuisine_type):
        """
        Initialize attributes of the parent class,
        then initialize attributes of the ice cream stand.
        """
        super().__init__(restaurent_name, cuisine_type)
        self.flavors = [
                        'caramel swirl', 'chocolate', 'vanilla',
                        'butterscotch', 'strawberry', 'coffee ripple'
                        ]
    def display_ice_creams(self):
        """Displays the different ice cream flavors."""
        for ice_cream in self.flavors:
            print(ice_cream)
            
my_ice_creams = IceCreamStand('havmor', 'ice cream')
my_ice_creams.display_ice_creams()
        
            
        
        
    
    
