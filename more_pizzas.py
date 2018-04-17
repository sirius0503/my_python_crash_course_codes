pizzas = [ 'spicy triple tango' , 'golden corn' , 'capsicum']

for pizza in pizzas:
	print( pizza.title() + " is one of my favourite pizzas \n")
print(" Well , I like pizzas of the kind with large toppings of italian cheese or something of the sort . And , I really hate loaded pizza . And , I don't really like pizza")

friend_pizzas = pizzas[:]

pizzas.append('margaritta')
friend_pizzas.append('pepperoni pizza')

print("\nMy favourite pizzas are:")
for pizza in pizzas:
	print(pizza)

print("\nMy friend's favourite pizzas are:")
for pizza in friend_pizzas:
	print(pizza)




