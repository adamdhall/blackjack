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
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
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

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

A = 11
J =  10
Q = 10
K = 10

deck = [A, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,J, Q, K]

from art import logo

import random

import replit

game_in_session = True

while game_in_session == True:

  print(logo)

  player_hand_1 = random.choice(deck)
  player_hand_2 = random.choice(deck)
  player_hand = player_hand_1 + player_hand_2

  dealer_hand_1 = random.choice(deck)
  print(f"your hand is {player_hand_1}, {player_hand_2}.")
  print(f"The dealer card is {dealer_hand_1}.")

  def hit():
    hit = input("Do you want another card? (y/n) ").lower()

    if hit == "y":
      another_card = random.choice(deck)
      player_hand += another_card
      return(f"You get a {another_card}, your hand total is now {player_hand}.")
      hit()
      

  hit()

  dealer_hand_2 = random.choice(deck)
  dealer_hand = dealer_hand_1 + dealer_hand_2
  print(f"The dealer has {dealer_hand_1} and {dealer_hand_2} for a total of {dealer_hand}")

  while dealer_hand < 17:
    another_dealer_card= random.choice(deck)
    dealer_hand += another_dealer_card
    print(f"The dealer draws a {another_dealer_card}, for a total of {dealer_hand}")

  
  print (f"Your total hand is {player_hand}")
  print(f"The dealer hand total is {dealer_hand}")

  if player_hand > dealer_hand:
    print("You win!")
  elif player_hand == dealer_hand:
    print("It's a tie!")
  elif player_hand > 21:
    print("you busted!")
  elif dealer_hand > 21:
    print("Delaer busts, you win!")
  else:
    print("You lose!")

  play_again = input("Would you like to play again? (y/n) ")


if play_again == "y":
  game_in_session == True
  replit.clear()
else:
  game_in_session == False

replit.clear()