dinner_guests = [ 'light yagami' , 'che guevara ' , 'zhang jike ' , 'ma long' ]
# It seems  che guevara can't make it to dinner :( 
print(dinner_guests)
absent = dinner_guests.pop(1)
dinner_guests.insert(1, "lelouch vi britannia")
print("\n Good day ,Mr." + (dinner_guests.pop()).title() + " you are cordially invited to my dinner party.")
print(" Good day ,Mr." + (dinner_guests.pop()).title() + " you are cordially invited to my dinner party.")
print(" Good day ,Mr." + (dinner_guests.pop()).title() + " you are cordially invited to my dinner party.")
print(" Good day ,Mr." + (dinner_guests.pop()).title() + " you are cordially invited to my dinner party.")
print(" For urgent reasons Mr." + absent.title() + " can't make it to the dinner party.")
