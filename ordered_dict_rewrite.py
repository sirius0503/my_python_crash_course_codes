from collections import OrderedDict

last_meaning = 'runs while loop till condition is True and then runs the else block'

glossary = OrderedDict()

glossary['class'] = 'representation of real world programming of things'
glossary['instances'] = 'the objects of the class'
glossary['PEP8'] = 'standard of styling python code'
glossary['modules'] = 'files in which we store classes'
glossary['functions'] = 'blocks of code which are meant for specific task'

"""for word, meaning in glossary.items():
    print(word.title() + "\n \t -- " + meaning + ".\n")"""
    
glossary['while loop'] = 'runs block of indented code till condition is True'
glossary['for loop'] = 'traverses through a list or dictionary for each item'
glossary['if statement'] = 'checks conditional statement to run block of code'
glossary['for else'] = 'runs for loop and then runs else code too'
glossary['while else'] = last_meaning

for word, meaning in glossary.items():
    print(word.title() + "\n \t -- " + meaning + ".\n")
    
