# Series of conditional tests.
# Checking for equality
anime = ['death note' , 'oregairu' ,'shinsekai yori' , 'another' ,'fate zero' \
,'monster' , 'steins gate' , 'xxxholic']
fav_anime = 'death note'

print("Is my favourite anime fav_anime == 'oregairu' ? I don't think so, \
even though I read the novels many times")
print( fav_anime == 'oregairu')

print("\nIs my favourite anime fav_anime = 'death note'? Most probably")
print( fav_anime == 'death note') 

#Checking for inequality
hobbies = ['studying' , 'playing TT' ,'python coding','watching anime','watch-\
ing movies','reading novel']
hobby = 'reading novel'

print("\nIs hobby != hobbies[0] ? 'Tis is true")
print(hobby != hobbies[0])

print("\nIs hobby != hobbies[5] ? 'Tis is false")
print(hobby != hobbies[5])

#Numerical Comparisons
age = 16
print("\nIs age >= 18 ? He will not get driving license")
print(age >= 18)

age = 29

print("\nIs age >= 18 ? He can get driving license ")
print(age >= 18)

#Checking multiple conditions using 'and' and 'or'
age1 = 19
age2 = 25
print("\nIs girl's age1 >= 18 and boy's age >= 21 ? They can get married")
print(age1 >=18 and age2 >= 21)

age1 = 16
age2 = 12
print("\nIs age1 < 18 or age2 < 18 ? Yes,they are both children")
print(age1 < 18 or age2 < 12)

#Checking whether a value is ina list ! Important!

users = ['john' ,'akriti' , 'jill' ,'harry' , 'anderson']
new_user = 'joey'
print("\nIs new_user in users ? He is new_user")
print(new_user in users)

new_user = 'akriti'

print("\nIs new_user in users ? yes ,change ur user_name")
print(new_user in users)

#Checking whether a value is not in a list
banned = ['andrew' , 'joseph','simons', 'persson' ,'alfred']
handle = 'mark'

print("\nIs handle not in banned ? yes, it's not banned")
print( handle not in banned )

