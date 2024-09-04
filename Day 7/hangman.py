# so we will be making a hangman game today
# what it does basically is that
# it randomly chooses a word and then asks you to guess it, you need to guess the letters in the word..
# if your guess matches any of the letter in the word, you get to guess for the next letter
# and if your guess doesnt match you lose a point

# import random
# print("Hello! Welcome to the Hangman")
# print("You have 5 lives")
# word_list=["hello","world","storage","full","birthday","print"]
# life=5
# word =random.choice(word_list)
# print("Start Guessing...")
# print("Your word is ....","_ "*len(word))
# userinp=input("Enter your guess here...  ")
# for i in word:
#     if i==userinp:
#         print("Yayyy! Your guess was right! Go on... Guess Further")
#     else:
#         print("Ohh no! Your guess was wrong! Try again...")
#         life-=1
#         print("You have ", life,"lives left")
# thoda irrelavant hai idhar but ek cheez samajh aayi aaj, ki bhai code likhne ka ek bohot bada part
# hai ye figure out karna ki ye build hoga kaise work kaise karega, kya logic run hona chahiye
# backend me.. toh jo chote projects hai uske liye toh dimaag me directly ho jaata hai but
# jo thoda complex ho jaata hai uske liye flowchart use karna shuru kar de bohot help ho jayga



# *****************************LETS START AGAIN*********************************
# so the game starts with boiler plate printing
# >>>>>>>>>> back end pe ek word list se randomly word select hota hai for
#  now random module nahi daalenge ham
# khud se word dalenge
# backend pe word select hoga or fir 
# >>>>>>>>>>>> uss word ka length print kar kisi bhi way me 
# >>>>>>>>>>>> ask the user to start guessing
# iske baad ka iske aage sochenge

chosenW="PASSWORD"
print("your word is...","_ "*len(chosenW))
game_over=False
display=""
while not game_over:
    print("You can start guessing in a while now...  ")

    # >>>>>>>>>>>> ab user input le usko lower/upper kar de 
    # >>>>>>>>>>>>> jo selected word hai usey split karke ek list me rakh le
    # ek for loop se userinput se list me check kar agar match ho rha hai toh
    chosenWord=chosenW.split()
    # print(chosenWord)
    userIp=input("Enter Your Guess Here: ")
    uInput=userIp.upper()
   correctLetter=[]

    for i in chosenW:
    
        if i==uInput:
        
            display+=i
            correctLetter.append(i)
            
        elif i in correctLetter:
            display+=i

        else:
            
            display+="_"
    print(display)
    # after initialising the loop we checked if the user input matches any of our letters, and then 
    # we even showed the rest of the word if the guess is right
    # ab kya karna hai?
    # do kaam hai pehla ki ye baar baar wrong right eliminate karna hai or doosra ki ye loop fir se chale...
    if "_" not in display:
        game_over=True
        print("You win")
    # abhi kya ho rha hai na while loop chal toh rha hai but for the 2nd time vo display ko append kar
    # rha hai toh aage or dash aa rhe hai replace nahi ho rhe