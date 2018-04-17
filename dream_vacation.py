#Polling users about their dream vacation

response = {}

prompt = "If you could visit one place in the world, where would you go? "

polling_active = True

while polling_active :
    name = input("\nPlease, cite your name: ")
    place = input(prompt)
    
    response[name] = place
    
    answer = input("\nWould you like to continue the poll :(yes/no) ")
    print("\n\n")
    
    
    if answer.lower() == 'no':
        polling_active = False

print("\n")
        

for name,place in response.items():
    print(name.title()+ " would like to visit " + place.title() + " atleast " +
        "once in a lifetime! " )
