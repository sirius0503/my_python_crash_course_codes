class Restaurent():
    """Typical information on a specific restaurent."""
    
    def __init__(self, restaurent_name, cuisine_type ):
        """Initialize name and cuisine attributes."""
        self.name = restaurent_name
        self.cuisine = cuisine_type
    
    def describe_restaurent(self):
        """Gives name & cuisine info about the restaurent."""
        print("\nThe restaurent is named: " + self.name.title())
        print("The restaurent serves: " + self.cuisine.title() + " cuisine.")
        
    def open_restaurent(self):
        """Message indicating that the restaurent is open."""
        print("\nThe restaurent is currently open!")
        
