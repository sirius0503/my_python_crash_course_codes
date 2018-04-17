from random import randint

class Die():
    """Representing a die with 'n' sides."""
    def __init__(self,side=6):
        """Initializing attribute side for the class Die."""
        self.sides = side
        
    def roll_die(self):
        """Gives the number on the die, after it has been rolled."""
        die_number = randint(1,self.sides)
        return die_number

six_sided_die = Die()
       
print("\nRolling a 6-sided die 10 times ,we get the following result.")
result = []

for key in range(10):
    """Retains the list of results."""
    result.append(six_sided_die.roll_die())

print(result)
result = []

#Making a 10 sided die

ten_sided_die = Die(10)

print("\nRollinga 10-sided die 10 times,we get the following result.")

for key in range(10):
    """Retains the list of results."""
    result.append(ten_sided_die.roll_die())
    
print(result)
result = []

#Making  a 20-sided die

twenty_sided_die = Die(20)

print("\nRolling a 20-sided die 10 times, we get the following results.")

for key in range(10):
    """Retains the list of results."""
    result.append(twenty_sided_die.roll_die())

print(result)
    
        
