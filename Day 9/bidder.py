# so sabse pehle the code runs and asks for the user's name
# and then it asks for the amount you want to bid
# and then it will ask if there are any more users
#  uske baad shuru hota hai code ka back end yaha pe..


# sabse pehle ek empty dictionary initialise kar de
# uske baad jitne bhi names hai unn sab ko keys add karte jaa
# or saath me unke amount ko values me daalte ja
#  ab fir saare values compare karo or unme se highest determine kar lo
import os
import art

main_dict={}
print(art.logo)
print("Hello Bidders! Let's Start Bidding....")
bidding_chalu=True
while bidding_chalu:
    
    name=input("apna naam daalo : ")
    bidding_amount=int(input("Please enter the amount in integers: "))
    main_dict[name]=bidding_amount
    z=input("Do you want to add anymore bidders? Input Yes or No: ").lower()
    os.system('cls')  # on windows
    os.system('clear')  # on linux / Mac
    if z=="no":
        bidding_chalu=False

highest_bidder = max(main_dict, key=main_dict.get) # I have no idea how this piece of code works but it just does
highest_bid =main_dict[highest_bidder]
print(f"This is the highest bid {highest_bid} from {highest_bidder}")
print(f"Congrats! {highest_bidder}... You have won the bid.")

