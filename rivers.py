rivers = {
    'nile' : 'egypt',
    'yellow river' : 'china' ,
    'mississippi river' : 'usa' ,
    }
for key,value in rivers.items():
    if value == 'usa':
         print("\nThe " + key + " river runs through " + value.upper() + " .")
    else :
        print("\nThe " + key + " river runs through " + value.title() + " .")

print("\n")


for key in rivers.keys():
    print(key.title())

print("\n")


for value in rivers.values():
    if value == 'usa':
        print(value.upper())
    else:
        print(value.title())
        
