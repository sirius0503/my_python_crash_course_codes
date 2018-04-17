def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())
        
def make_great(list_of_magicians):
    for key in range(len(list_of_magicians)):
        list_of_magicians[key] = 'the great ' + list_of_magicians[key]
    return list_of_magicians



magician_names = ['harry houdini','criss angel','david copperfield','david \
blaine','teller','dynamo','derren brown' , 'p.c. sorcar']

show_magicians(make_great(magician_names))


        

        
