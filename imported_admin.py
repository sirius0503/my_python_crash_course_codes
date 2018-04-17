from admin import Privileges

powers = ['is superuser', 'can login to root', 'can delete user accounts']
powers += ['can add new users', 'can change password']

Admin = Privileges(privileges =powers)
Admin.show_privileges()
