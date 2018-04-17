class User():
    """User profile buildup."""
    
    def __init__(self, first, last, city, hobby):
        """Initialize first and last names."""
        self.first_name = first
        self.last_name = last
        self.city = city
        self.hobby = hobby
        self.login_attempts = 0
        
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
    def increment_login_attempts(self):
        """Increments the value of login_attempts by 1."""
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        """Resets the value of login_attempts to 0."""
        self.login_attempts = 0
        
chaudhary = User('rishabh', 'chaudhary', 'gurgaon', 'table tennis')
i = 4
while i > 0 :
    chaudhary.increment_login_attempts()
    print("Login attempts: " + str(chaudhary.login_attempts) )
    i -= 1 
    
chaudhary.reset_login_attempts()
print("\nLogin attempts: " + str(chaudhary.login_attempts))
    

