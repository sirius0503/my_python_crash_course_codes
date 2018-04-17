prompt = "Please, enter a number and I'll report something interesting about "
prompt += "\nthe number! "

number = input(prompt)
number = int(number)

if number % 10 == 0 :
    print("\nThe number is a multiple of 10.")
else:
    print("\nThe number isn't a multiple of 10")
