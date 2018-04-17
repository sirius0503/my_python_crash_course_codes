current_users =  ['admin' ,'Aspiring1' ,'james' ,'harry' ,'helena','eric','chan\
dler']
current_users1 = [ user.lower() for user in current_users ]

new_users = ['james','matthew','Helena','Dhoni' ,'martin']

for user in new_users:
    if user.lower() in current_users1 :
        print("\nUser name not available , please enter a new user name")
    else:
        print("\nUser name is available")
        



