def censor ( text , word ) :
    word_len = len(word)
    list = [] 
    index = 0
    index2 = 0
    for char in text :
        if char == " ":
            list.append(text[index2 : index])
            index2 = index + 1
        index += 1
    print list
    for i in range(len(list)):
        if list[i] == word:
            list[i] = '*' * word_len
    p = " ".join(list)
    return p
print censor("this hack is wack hack", "hack")
