def make_shirt(message_text='I love Python' , size='Large'):
    """"Prints a message summarizing the size of the shirt and the message 
        printed on it"""
    size_string = "'" + str(size) + "'"
    print("\nThe size of the T-Shirt is " + size_string +
        " and the message written on it is " + message_text + ".")
        
make_shirt()
make_shirt(size='Medium')
make_shirt(message_text='Monty Python made python' , size='Small')

