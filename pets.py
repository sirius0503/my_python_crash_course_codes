tommy = {
    'kind' : 'dog',
    'owner' : 'Mr.Smith',
    }

Nanny = {
    'kind' : 'cow',
    'owner' : 'martha',
    }

Mammy = {
    'kind' : 'goat',
    'owner': 'isabelle',
    }
    
rolly = {
    'kind' : 'monkey',
    'owner': 'nick',
    }

smuff = {
    'kind' : 'koala',
    'owner': 'andrew',
    }
pets = [tommy ,Nanny, Mammy, rolly , smuff]

for pet in pets:
    print("\n" + pet['owner'].title() + " has a pet " + pet['kind'].title() +
        "."
        )
        
