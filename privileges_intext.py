class User():
    """User profile buildup."""
    
    def __init__(self, first, last, city, hobby):
        """Initialize first and last names."""
        self.first_name = first
        self.last_name = last
        self.city = city
        self.hobby = hobby
        self.login_attempts = 0
        self.privileges = Privileges()
                            
        
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
    
            
class Privileges():
    """ A admin's privileges class."""
    def __init__(self, privileges=[ 'can add post', 'can delete post',
                                    'can ban user','can add user', 
                                    'can mute user']):
        """Enter the privileges of the admin or accept the default values"""
        self.privileges = privileges
        
    
    def show_privileges(self):
        """
        Prints the privileges of the administrator.
        """
        print("\nAdministrator privileges: ")
        for privilege in self.privileges:
            print("- " + privilege)
            
            
Admin = User('sauranil', 'debarshi', 'guwahati', 'football')
Admin.privileges.show_privileges()
print("\t" + Admin.first_name.title())
            

