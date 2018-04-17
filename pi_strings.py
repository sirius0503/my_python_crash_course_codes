filename = '/home/aspiring1/Downloads/ehmatthes-pcc-f063320/chapter_10/pi_m'
filename += 'illion_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()
    
print(pi_string[:52] + "...")
print(len(pi_string))
