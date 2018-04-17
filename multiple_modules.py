from privileges import Privileges

power = ["doesn't have much to do", 'can sleep tight', 'has to know linux']
power += ['has to have linux installed to be one']

Admin = Privileges(power)
Admin.show_privileges()
