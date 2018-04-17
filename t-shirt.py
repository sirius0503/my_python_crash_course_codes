def make_shirt(size ,message_text):
    """"Prints a message summarizing the size of the shirt and the message 
        printed on it"""
    size_string = "'" + str(size) + "'"
    print("\nThe size of the T-Shirt is " + size_string +
        " and the message written on it is " + message_text + ".")
        
make_shirt('Medium ', "'Stack Exchange'")
make_shirt(message_text="'Evil rises again'",size='Small')
        
        
