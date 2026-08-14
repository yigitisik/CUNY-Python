import art, random

print(art.logo)
play_game = True
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def get_score(card_set):
    score = sum(card_set)
    # Handle the Ace (11 becomes 1 if score exceeds 21)
    if 11 in card_set and score > 21:
        card_set.remove(11)
        card_set.append(1)
        score = sum(card_set)
    return score

"""set_1 is player and set_2 is dealer"""
def score_comparison(set_1, set_2):
    score_1 = get_score(set_1)
    score_2 = get_score(set_2)
    print(f"Your hand: {set_1}, your score: {score_1}")
    print(f"Dealer's  hand: {set_2}, dealer's score: {score_2}")
    if score_1 > 21:
        return "You went over 21! You lose."
    elif score_2 > 21:
        return "Dealer went over 21! You win!"
    elif score_1 == score_2:
        return "It's a draw"
    if score_1 > score_2:
        return "You win!"
    else:
        return "You lose :/"

while play_game:
    dealer_set = []
    player_set = []
    print()
    resume_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if resume_choice.lower()=="n":
        play_game = False
        break

    player_set.extend([random.choice(cards) for _ in range(2)])
    dealer_set.extend([random.choice(cards) for _ in range(2)])  # Dealer gets 2 cards

    print(f"Your cards: {player_set}, current score: {get_score(player_set)}")
    print(f"Dealer's first card: {dealer_set[0]}")

    #Player's turn
    while True:
        card_add_choice = input("\nType 'y' to get another card, type 'n' to pass:")
        if card_add_choice.lower()=="y":
            player_set.append((random.choice(cards)))
            print(f"Your cards: {player_set}, current score: {get_score(player_set)}")
            if get_score(player_set) > 21:
                print("Went over, you lose :/")
                break
        else:
            break

    # Dealer's turn: Dealer draws until their score is 17 or more
    while get_score(dealer_set) < 17:
        dealer_set.append(random.choice(cards))

    #Final Stand
    if get_score(player_set) <= 21:
        game_status = score_comparison(player_set, dealer_set)
        print(game_status)
