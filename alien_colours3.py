alien_colour = 'red'
points = 0

if alien_colour == 'green':
    points = 5
elif alien_colour == 'yellow':
    points = 10
elif alien_colour == 'red':
    points = 15
else:
    pass
print("\nYou have just earned " + str(points) + " points for shooting \
the alien")
    
