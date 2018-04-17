# Using a conditional test to stop the while loop

ticket = ""
total_tickets = 5
while total_tickets != 0:
    age = input("\nPlease,enter your age: ")
    age = int(age)
    if age < 3 :
        ticket = '0 $'
    elif age >= 3 and age < 12 :
        ticket = '10 $'
    else:
        ticket = '15 $'
    print("The cost of your movie ticket is: " + ticket)
    total_tickets -= 1

#Using an active variable to control how long the loop runs    

ticket = ""
current = 1 
active = True
while active:
    age = input("\nPlease,enter your age: ")
    age = int(age)
    if age < 3 :
        ticket = '0 $'
    elif age >= 3 and age < 12 :
        ticket = '10 $'
    else:
        ticket = '15 $'
    print("The cost of your movie ticket is: " + ticket)
    current += 1
    if current > 5:
        active = False
    
    ticket = ""
while True:
    age = input("\nPlease,enter your age: ")
    age = int(age)
    if age < 3 :
        ticket = '0 $'
    elif age >= 3 and age < 12 :
        ticket = '10 $'
    else:
        ticket = '15 $'
    print("The cost of your movie ticket is: " + ticket)

#Using a break statement to exit the loop when the user enters a 'quit' value

ticket = ""
while True:
    age = input("\nPlease,enter your age: ")
    if age == 'quit':
        break
    age = int(age)
    if age < 3 :
        ticket = '0 $'
    elif age >= 3 and age < 12 :
        ticket = '10 $'
    else:
        ticket = '15 $'
    print("The cost of your movie ticket is: " + ticket)

    


