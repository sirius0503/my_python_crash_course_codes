filename = 'text_files/learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    
for line in lines:
    print(line.replace('Python', 'Ruby').rstrip())
    
