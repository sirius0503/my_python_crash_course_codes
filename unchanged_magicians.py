def show_magicians(magicians):
    """Prints the name of magicians in list magicians"""
    for magician in magicians:
        print(magician.title())

        
def make_great(list_of_magicians):
    """Prints the list of magicians with the string 'the Great' appended
    with each item"""
    for key in range(len(list_of_magicians)):
        list_of_magicians[key] = 'the great ' + list_of_magicians[key]
    return list_of_magicians


magician_names = ['harry houdini','criss angel','david copperfield','david \
blaine','teller','dynamo','derren brown' , 'p.c. sorcar']

new_list = make_great(magician_names[:])

show_magicians(magician_names)

print("\n")

show_magicians(new_list)
