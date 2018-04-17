active = True 
prompt = "\nPlease,enter pizza topping that you want to add to your "
prompt += "pizza one at a time,\nIf you're done with the toppings,enter 'quit'\
  "


while active:
    topping = input(prompt)
    if topping == 'quit':
        active = False
    else:
        print("\nWe'll be adding " + topping.title() + " to your pizza!")
   
    
