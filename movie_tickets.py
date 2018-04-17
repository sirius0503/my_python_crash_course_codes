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
