run = True

filename = 'text_files/guest_book.txt'

while run :
    #Run while loop for prompt of user till he wants to quit
    
    name = input("\nGood morning, what is your good name: ")
    print("<---to quit, enter 'q'--->")
    
    if name == 'q':
        run = False
    else:
        print("Hello, " + name.title() + " hope you have a splendid stay!")
        
        with open(filename, 'a') as file_object:
            file_object.write(name.title() + "\n")

    
    
