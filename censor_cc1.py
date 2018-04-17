def censor(text, word):
    new_string_array = []
    text = text.split()
    m = "*" * len(word)
    for i in text:
         if i == word:
             print new_string_array.append(m)
         else:
              new_string_array.append(i)
    var = " ".join(new_string_array)
    return var
print(censor("hey hey hey",'hey'))

