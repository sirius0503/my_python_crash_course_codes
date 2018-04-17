glossary = {
    'split' : 'splits a string into a list',
    'in' : 'used to find whether variable is in list or not',
    'for': 'used to iterate a block of commands',
    'list':'a collection of strings , numbers ,etc like arrays',
    'if': 'statement verifies condition to execute code',
    }
    
glossary['.items()'] = 'gives us the key ,value pair from dictionaries'
glossary['.keys()'] = 'supplies us the keys in a dictionary'
glossary['.values()'] = 'supplies us the values in a dictionary'
glossary['for else'] = 'for else loop ends with else executed too ,unless \
a break is  executed in the for loop'
glossary['while'] = ' loops till condition is falsified '


for key,value in glossary.items():
    print("\n" + key + " : " + value)

