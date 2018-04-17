my_foods = ['pizza' , 'falafel' , 'carrot cake']
# This doesn't work
friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favourite foods are:")
print(my_foods)

print("\nMy friend's favourite foods are:")
print(friend_foods)

""" Instead of storing a copy of my_foods in friend_foods ,we set 
friend_foods equal to my_foods. This syntax actually tells Python to 
connect the new variable friend_foods to the list that is already 
contained in my_foods, so now both variables point to the same list.
As a result, when we add 'cannoli' to my_foods, it will also appear in 
friend_foods. Likewise 'ice cream' will appear in both lists, even 
though it appears to be added only to friend_foods."""
