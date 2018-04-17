favorite_numbers = {
    'resda' : [ 44, 23 ],
    'Johnny' : [ 9 , 10 , 8 , 22 , 46 ],
    'Kefda' : [11],
    'markewadi' : [51 , 52],
    'Palu ho' : [34 , 37]
    }
    
for name , num in favorite_numbers.items():
    if len(num) == 1:
        print("\n" + name.title() + "'s favorite number is: " )
    else:
        print("\n" + name.title() +"'s favorite numbers are : " )
    print("\t")
    for key in num:
        print( str(key) ) ,
    print("\n")
            
