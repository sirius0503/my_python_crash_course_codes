a = 2

def plusOne2(a):
    a += 1
    return a

print (plusOne2(a)),
print( a)

"""y = [1,2,3]

def plusOne(y):
    for x in range(len(y)):
        y[x] += 1
    return y

print plusOne(y), y


a = 2

def plusOne2(a):
    a += 1
    return a

print plusOne2(a), a
Values of 'y' change but value 'a' stays the same. I have already learned that
 it's because one is mutable and the other is not. But how to change the code
  so that the function doesn't change the list?
"""

"""Python variables contain pointers, or references, to objects. All values 
(even integers) are objects, and assignment changes the variable to point to 
a different object. It does not store a new value in the variable, it changes 
the variable to refer or point to a different object. For this reason many 
people say that Python doesn't have "variables," it has "names," and 
the = operation doesn't "assign a value to a variable," but rather 
"binds a name to an object."

In plusOne you are modifying (or "mutating") the contents of y but never change
 what y itself refers to. It stays pointing to the same list, the one you 
 passed in to the function. The global variable y and the local variable y
refer to the same list, so the changes are visible using either variable.
Since you changed the contents of the object that was passed in, there is 
actually no reason to return y (in fact, returning None is what Python 
itself does for operations like this that modify a list "in place" 
-- values are returned by operations that create new objects rather 
than mutating existing ones).

In plusOne2 you are changing the local variable a to refer to a different integer object, 3. ("Binding the name a to the object 3.") The global variable a is not changed by this and continues to point to 2.

If you don't want to change a list passed in, make a copy of it and change that. Then your function should return the new list since it's one of those operations that creates a new object, and the new object will be lost if you don't return it. You can do this as the first line of the function: x = x[:] for example (as others have pointed out). Or, if it might be useful to have the function called either way, you can have the caller pass in x[:] if he wants a copy made.
"""
