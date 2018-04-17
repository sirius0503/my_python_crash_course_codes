filename = 'text_files/learning_python.txt'
"""
with open(filename) as file_object:
    contents = file_object.read()

for num in range(3):
    print(contents)
"""
 
for num in range(3):
    with open(filename) as file_object:
        for line in file_object:
            print(line.rstrip())

"""with open(filename) as file_object:
    lines = file_object.readlines()
    
for num in range(3):
    for line in lines:
        print(line.rstrip())"""
