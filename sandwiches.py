def sandwich(*fillings):
    """Prints out the different kinds of fillings inside a sandwich and takes 
    variable number of arguments"""
    print("\nThe sandwich has the following fillings: ")
    for filling in fillings:
        print("-" + filling)
        
sandwich('egg mayo ' , 'tuna mayo' ,'cheese & mango chutney')
sandwich('cream cheese & strawberries' ,'pulled lamb')
sandwich('california veggies')
