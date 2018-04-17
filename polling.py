favorite_languages = {
    'jen' : 'python' ,
    'sarah' : 'c' ,
    'edward' : 'ruby' ,
    'phil' : 'python' ,
    }
    
    
for name,language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + 
        language.title() + " ."
        )
        
#People who should take the favourie languages poll!

people = [ 'erin ' , 'james' , 'sarah' ,'ed' , 'paul' ,'phil']

print("\n")

for name in people:
    if name in favorite_languages.keys():
        print(name.title() + " : Thank,you for responding to our poll. " )
    else:
        print(name.title() + " please,take our favorite languages poll." )
