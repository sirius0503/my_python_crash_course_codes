def anti_vowel ( text ):
    vowel = 'aeiouAEIOU'
    m = []
    for i in range(len(text)):
        for char in vowel :
            if text[i] == char:
                break 
        else:
            m.append(text[i])
            q = "".join(m)
    return q
print anti_vowel( "Hey look ,who's here")
