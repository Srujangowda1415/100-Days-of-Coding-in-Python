# so the game starts with a welcome message
# and then it asks you to press start key whenever you are ready
# backend pe ek list bana cards ki
# game start hote hi... user ko 2 cards randomly assign kar or vo show bhi honge
# computer ko 2 cards assign karo but show ek hi hoga
# user ke cards ka sum show karo
# ab ask user if he wants to hit or stand
#  if he hits then ek or card assign karo or fir sum show karo
# computer ko bhi assign hoga ek card
# fir se hit kiya toh the moment it goes over 21 toh you lose
# agar stand kiya toh computer or user score check karo jiska high hua vo jeet gaya
import random
welcome_message="Hello User! Have fun playing this little game"
start_message=input("hit enter to start the game")
should_continue=True
if start_message=="":
    cards=[1,2,3,4,5,6,7,8,9,10,11]
    user_cards=[]
    dealer_cards=[]
    user_score=0
    dealer_score=0
    x=random.randint(1,11)
    user_cards.append(x)
    x=random.randint(1,11)
    user_cards.append(x)
    y=random.randint(1,11)
    dealer_cards.append(y)
    y=random.randint(1,11)
    dealer_cards.append(y)
    user_score=sum(user_cards)
    dealer_score=sum(dealer_cards)
    dealer_first_score=dealer_score
    print(f"These are your cards:{user_cards} and this is your score:{user_score}")
    print(f"{dealer_cards[0]} this is dealer's first card")
    while user_score<21 and should_continue:
        cont=input("hit 'h' to hit or 'n' to stand").lower()
        if cont=="h":
            x=random.randint(1,11)
            user_cards.append(x)
            y=random.randint(1,11)
            dealer_cards.append(y)
            user_score=sum(user_cards)
            dealer_score=sum(dealer_cards)
            print(user_score,"This is your score")
            
            print(dealer_cards[0],"this is dealer's first score")
        elif cont=="n":
            y=random.randint(1,11)
            dealer_cards.append(y)
            user_score=sum(user_cards)
            dealer_score=sum(dealer_cards)
            print(user_score,"This is your score")
            print(dealer_score,"this is dealer's score")
            if dealer_score>user_score:
                print("You lose!")
                print("It was nice having you here... See you soon...")
                should_continue=False
            elif user_score>dealer_score:
                print("You win")
                print("It was nice having you here... See you soon...")
                should_continue=False
            
        
    print("You lose")
    print("It was nice having you here... See you soon...")
    should_continue=False



               



else:
    print("It was nice having you here... See you soon...")
