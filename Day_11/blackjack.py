import random
from art import logo
from replit import clear

# uses card List below to *return* a random card.
def deal_card():
    """Return a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(list):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(list) == 21 and len(list) == 2:
        return 0

    if 11 in list and sum(list) > 21:
        list.remove(11)
        list.append(1)
    return sum(list)

def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose"
    
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Computer got blackjack! You lose"
    elif user_score == 0:
        return "You got blackjack. You win!"
    elif user_score > 21:
        return "You went over, you lose!"
    elif computer_score > 21:
        return "Computer went over, you win!"
    elif user_score > computer_score:
        return "You beat the computer. You win!"
    elif computer_score > user_score:
        return "Computer beat you. You lose"
    else:
        return "You lose"


def play_blackjack():
    print(logo)
    
    user_cards = []
    computers_cards = []
    is_game_over = False
    
    for _ in range(2):
        user_cards.append(deal_card())
        computers_cards.append(deal_card())
    
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computers_cards)
        
        print(f"Your cards are {user_cards}, current score: {user_score} \n Computer's first card: {computers_cards[0]}")
        
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'yes' to get another card, type 'no' to pass: ").lower()
            if user_should_deal == "yes":
                user_cards.append(deal_card())
            else:
                is_game_over = True
                
    while computer_score != 0 and computer_score < 17:
        computers_cards.append(deal_card())
        computer_score = calculate_score(computers_cards)
    
    print(f"Your final hand: {user_cards}, current score: {user_score} \nComputer's final hand: {computers_cards}, current score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'yes' or 'no'").lower() == 'yes':
    clear()
    play_blackjack()


