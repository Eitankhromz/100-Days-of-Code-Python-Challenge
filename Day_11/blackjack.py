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

    OR
    
############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:

## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

import random
from replit import clear
from art import logo

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
  """Deals a random card"""
  return random.choice(cards)


#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.
def calculate_score(cards):
  """Checks for blackjack. Checks for an ace. Returns current score."""
  #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
  score = sum(cards)
  length = len(cards)
  if score == 21 and length == 2:
    return 0

  #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
  for card in cards:
    if score > 21 and card == 11:
      cards.remove(11)
      cards.append(1)
  
  return sum(cards)



#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(current_user_score, current_computer_score):
  if current_user_score> 21 and current_computer_score > 21:
    return "You Lose! You went over!"
    
  if current_user_score == current_computer_score:
    return "It's a draw."
  elif current_computer_score == 0:
    return "You lose! Dealer got blackjack."
  elif current_user_score == 0:
    return "You win! You got blackjack"
  elif current_user_score > 21:
    return "You went over! You lose"
  elif current_computer_score > 21:
    return "Dealer went over! You win!"
  elif current_user_score > current_computer_score:
    return "You have a higher score! You win!"
  else:
    return "Dealer has a higher score. You lose!"

def blackjack():
  #Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
  print(logo)

  #Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
  user_cards = []
  computer_cards = []
  play_blackjack = False
  
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

    
  while not play_blackjack:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      play_blackjack = True
      #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
    else:
      draw_card = input("Type 'y' to get another card, type 'n' to pass: ")
      if draw_card == 'y':
        user_cards.append(deal_card())
      elif draw_card == 'n':
        play_blackjack == True
  
  
    #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
  while computer_score < 17 and computer_score != 0:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"Your final hand: {user_cards}, final score: {user_score}")
  print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))


#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
  clear()
  blackjack()
 

