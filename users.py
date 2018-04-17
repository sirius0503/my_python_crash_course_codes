class User():
    """User profile buildup."""
    
    def __init__(self, first, last, city, hobby):
        """Initialize first and last names."""
        self.first_name = first
        self.last_name = last
        self.city = city
        self.hobby = hobby
        
    def describe_user(self):
        """Summary of user's information."""
        print("\nThe user's first name is: " + self.first_name.title() +
            "\nThe user's last name is: " + self.last_name.title() )
        print("He lives in " + self.city.title() + " and his personal hobby is " +
            self.hobby.title() + "."
            )
            
    def greet_user(self):
        """Prints personalized greeting to the user."""
        print("\nHello, " + self.first_name.title() + " " + 
            self.last_name.title() +
            "!")
            
rishabh = User('rishabh', 'chaudhary','gurgaon','table tennis')
johnny = User('johnny', 'anubhav sins', 'allahabad', 'watching movies')
markewadi = User('markewadi', 'pipliwal', 'jaipur', 'coding')

rishabh.describe_user()
rishabh.greet_user()

johnny.describe_user()
johnny.greet_user()

markewadi.describe_user()
markewadi.greet_user()
