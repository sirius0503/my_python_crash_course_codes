simple_foods = ( 'rice' ,'roti' ,'mixed veg' , 'paneer' , 'dal')

print("Restaurent menu is as follows:")
for food in simple_foods:
    print(food.title())
    
#simple_foods[1] = 'pav bhaji'

#Restaurent changes its menu ;
simple_foods = ('rice' ,'roti' ,'paneer tikka masala' , 'shahi paneer' ,'dal')

print("\nNew changed restaurent menu")
for food in simple_foods:
    print(food.title())

