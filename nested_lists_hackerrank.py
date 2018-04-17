grades =[]
for key in range(int(input())):
    name = input()
    score = float(input())
    list = [name ,score ]
    grades.append(list)
def lowest(marks):
    key = marks[0][1]
    print(key)
    person = []
    for num in marks:
        if num[1] < key:
            key = num[1]
    for num in marks:
        if num[1] == key:
            person.append(num[0])
            marks.remove(num)
        n += 1
    print(marks)
    print(person)
    return person
d = []
l = lowest(grades)
d.append(lowest(grades))
d.append(lowest(grades))
d.sort()


    
