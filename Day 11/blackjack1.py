import random

welcome_message = "Hello User! Have fun playing this little game"
print(welcome_message)

start_message = input("Hit enter to start the game: ")

if start_message == "":
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    user_cards = []
    dealer_cards = []
    user_score = 0
    dealer_score = 0
    should_continue = True

    # Deal initial cards
    user_cards.append(random.choice(cards))
    user_cards.append(random.choice(cards))
    dealer_cards.append(random.choice(cards))
    dealer_cards.append(random.choice(cards))

    # Calculate initial scores
    user_score = sum(user_cards)
    dealer_score = sum(dealer_cards)
    dealer_first_score = dealer_cards[0]

    print(f"These are your cards: {user_cards} and this is your score: {user_score}")
    print(f"{dealer_cards[0]} this is dealer's first card")

    while user_score < 21 and should_continue:
        cont = input("Hit 'h' to hit or 'n' to stand: ").lower()

        if cont == 'h':
            user_cards.append(random.choice(cards))
            user_score = sum(user_cards)
            print(f"These are your cards: {user_cards} and this is your score: {user_score}")

        elif cont == 'n':
            # Dealer draws cards until their score is 17 or higher
            while dealer_score < 17:
                dealer_cards.append(random.choice(cards))
                dealer_score = sum(dealer_cards)

            print(f"Dealer's cards: {dealer_cards} and score: {dealer_score}")

            if dealer_score > 21:
                print("Dealer busts! You win!")
            elif user_score > dealer_score:
                print("You win!")
            elif user_score < dealer_score:
                print("Dealer wins!")
            else:
                print("It's a tie!")

            should_continue = False

    if user_score > 21:
        print("You bust! Dealer wins.")

    print("Thank you for playing!")
else:
    print("It was nice having you here... See you soon...")