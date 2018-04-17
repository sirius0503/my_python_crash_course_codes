filename = '/home/aspiring1/Downloads/ehmatthes-pcc-f063320/chapter_10/pi_mi'
filename += 'llion_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    
pi_string = ''
for line in lines:
    pi_string += line.rstrip()
    
birthday = input("Enter your birthday in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday doesn't appear in the first million digits of pi")
