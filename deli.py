sandwich_orders = ['French dip' , 'Egg salad','The Dagwood' ,'The Caprese']
sandwich_orders +=['Clam roll' , 'Ham and cheese','The Jibarito','Bologna \
sandwich']
sandwich_orders.reverse()

finished_sandwiches = []

while sandwich_orders :
    current_sandwich = sandwich_orders.pop()
    if 'sandwich' in current_sandwich :
        print("\nI made your " + current_sandwich + ".")
    else:
        print("\nI made your " + current_sandwich + " sandwich.")
    

    
    finished_sandwiches.append(current_sandwich)
        
        
print("\n\t----SANDWICHES---MADE-----\n")

for sandwich in finished_sandwiches:
    print(sandwich)
        
        
