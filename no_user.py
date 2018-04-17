names = []

if names :
    for user in names :
        if user == 'admin':
            print("Hello admin,would you like to see a status report?\n")
        else:
            print("Hello " + user + ", thank you for logging in again \n")
else:
    print("We need to find some users!")
        
    
