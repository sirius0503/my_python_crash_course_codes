person1 = {
    'first_name' : 'albert' ,
    'last_name' : 'einstein' ,
    'city' : 'princeton',
    }
    
person2 = {
    'first_name' : 'marie',
    'last_name' : 'curie',
    'city' : 'paris',
    }
    
people = [ person1 , person2 ]

for person in people:
    full_name = person['first_name'] + " " + person['last_name']
    location = person['city']
    print("\n Mr.\Ms. " + full_name.title() + " is currently stationed at : \n \t" +
        location.title() + "."
        )
