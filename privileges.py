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
