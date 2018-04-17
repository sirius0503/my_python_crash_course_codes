def reverse ( text ):
    list = []
    length = len(text) - 1 
    while length >= 0 :
        list.append(text[length])
        length -= 1
    print "".join(list) ,
reverse("Python!")
        
