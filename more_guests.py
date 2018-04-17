dinner_guests = [ 'light yagami' , 'che guevara ' , 'zhang jike ' , 'ma long' ]
# It seems  che guevara can't make it to dinner :( 
print(dinner_guests)
absent = dinner_guests.pop(1)
dinner_guests.insert(1, "lelouch vi britannia")
print("\n Good day ,Mr." + dinner_guests[0].title() + " you are cordially invited to my dinner party.")
print(" Good day ,Mr." + dinner_guests[1].title() + " you are cordially invited to my dinner party.")
print(" Good day ,Mr." + dinner_guests[2].title() + " you are cordially invited to my dinner party.")
print(" Good day ,Mr." + dinner_guests[3].title() + " you are cordially invited to my dinner party.")
print(" For urgent reasons Mr." + absent.title() + " can't make it to the dinner party.")

# More Guests

print(" \n \t I have fortunately found a bigger dinner table & so will be inviting a few more esteemed guests to make the event merrier")
dinner_guests.insert(0 , 'monty python')
dinner_guests.insert(int(len(dinner_guests)/2 ), 'emma stone')
dinner_guests.append('kristen stewart')
print("\n")
print(dinner_guests)
print("\n Good day ,Mr." + (dinner_guests.pop()).title() + " you are cordially invited to my dinner party.")
print(" Good day ,Mr." + (dinner_guests.pop()).title() + " you are cordially invited to my dinner party.")
print(" Good day ,Mr." + (dinner_guests.pop()).title() + " you are cordially invited to my dinner party.")
print(" Good day ,Mr." + (dinner_guests.pop()).title() + " you are cordially invited to my dinner party.")
print(" Good day ,Mr." + (dinner_guests.pop()).title() + " you are cordially invited to my dinner party.")
print(" Good day ,Mr." + (dinner_guests.pop()).title() + " you are cordially invited to my dinner party.")
