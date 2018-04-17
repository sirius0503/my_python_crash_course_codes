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
print("\n Good day ,Mr.\Ms. " + dinner_guests[0].title() + " you are cordially invited to my dinner party.")
print(" Good day ,Mr.\Ms. " + dinner_guests[1].title() + " you are cordially invited to my dinner party.")
print(" Good day ,Mr.\Ms. " + dinner_guests[2].title() + " you are cordially invited to my dinner party.")
print(" Good day ,Mr.\Ms. " + dinner_guests[3].title() + " you are cordially invited to my dinner party.")
print(" Good day ,Mr.\Ms. " + dinner_guests[4].title() + " you are cordially invited to my dinner party.")
print(" Good day ,Mr.\Ms. " + dinner_guests[5].title() + " you are cordially invited to my dinner party.")
print(" Good day ,Mr.\Ms. " + dinner_guests[6].title() + " you are cordially invited to my dinner party.")

""" New info suggests the new dinner table won't be arriving in time for the dinner,
and I have space for only two guests"""

print("\n Sorry to say this ,but it looks like I can only accomodate only two guests for the evening ")
print(" \n  I am sorry Mr.\Ms. " + (dinner_guests.pop()).title() + "  I won't be able to accomodate you for dinner this evening ,due to unavoidable reasons")
print("   I am sorry Mr.\Ms. " + (dinner_guests.pop()).title() + "  I won't be able to accomodate you for dinner this evening ,due to unavoidable reasons")
print(" \n  I am sorry Mr.\Ms. " + (dinner_guests.pop()).title() + "  I won't be able to accomodate you for dinner this evening ,due to unavoidable reasons")
print(" \n  I am sorry Mr.\Ms. " + (dinner_guests.pop()).title() + "  I won't be able to accomodate you for dinner this evening ,due to unavoidable reasons")
print(" \n  I am sorry Mr.\Ms. " + (dinner_guests.pop()).title() + "  I won't be able to accomodate you for dinner this evening ,due to unavoidable reasons")

#Printing messages for people who are still invited

print("\n Dear , Sir/Madam " + dinner_guests[0].title() + " you are still on the invitation list of my party and I would be eagerly awaiting for your presence in the party")
print("\n Dear , Sir/Madam " + dinner_guests[1].title() + " you are still on the invitation list of my party and I would be eagerly awaiting for your presence in the party \n")
del dinner_guests[0]
del dinner_guests[0]
print (dinner_guests)
