run = True
filename = 'text_files/programming_poll.txt'

while run:
    """ Loop records reasons why people like programming."""
    reason = input("\nPlease,tell us your reason for enjoying programming: ")
    print("<-----To quit at anytime--enter---'q'---as the reason.")
    
    if reason == 'q':
        run = False
    else:
        with open(filename, 'a') as file_object:
            file_object.write(reason + "\n")
    
