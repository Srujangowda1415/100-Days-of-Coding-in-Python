# so we will be creating a password generator today
#  we will first define a list of alphabets,numbers and then special characters
# and then we ask the user for the number of alphabets, number of numbers and number of special characters
# after that we create for loops to pick random alphabets, numbers, special characters and then append them ek ek karke respectively

import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*','(',')']

print("Hello! Welcome to the Password Generator... Happy Generating...")
print(" Kindly Answer the following questions")
noletter=int(input("Enter the number of letters you want in your password...  "))
nocapletter=int(input("Enter the number of capital letters you want in your password...  "))

nonumber=int(input("Enter the number of numbers you want in your password...  "))
nosymbol=int(input("Enter the number of symbols you want in your password... "))

password=''

for i in range(1,noletter+1):
    password+=random.choice(letters)

for i in range(1,nocapletter+1):
    capletter= (random.choice(letters))
    password+=capletter.capitalize()

for i in range(1,nonumber+1):
    password+=random.choice(numbers)

for i in range(1,nosymbol+1):
    password+=random.choice(symbols)

# print(password)
l = list(password)
random.shuffle(l)
result = ''.join(l)
print(result)