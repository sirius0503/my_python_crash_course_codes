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
        
        
restaurent = Restaurent('yukihara', 'japanese')
print(restaurent.name.title())
print(restaurent.cuisine.title())
print(restaurent.number_served)
restaurent.set_number_served(14)
print(restaurent.number_served)
restaurent.increment_number_served(5)
print(restaurent.number_served)

restaurent.describe_restaurent()
restaurent.open_restaurent()


