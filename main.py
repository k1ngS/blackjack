import random
from replit import clear
from art import logo

def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)

def calculate_score(cards):
  """Take a lis of cards and return the score calculared from the cards"""
  
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  if user_score == computer_score:
    return "  Draw\n"
  elif computer_score == 0:
    return "  Lose, Dealer's has Blackjack\n"
  elif user_score == 0:
    return "  Win with a Blackjack\n"
  elif user_score > 21:
    return "  You went over. You lose\n"
  elif computer_score > 21:
    return "  Dealer's went over. You win\n"
  elif user_score > computer_score:
    return "  You Win\n"
  else:
    return "  You lose\n"

def play_game():

  print(logo)

  user_cards = []
  computer_cards = []
  is_game_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not is_game_over:

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print("-"*55)
    print(f"Your Cards: {user_cards}")
    print(f"current score: {user_score}\n")
    print(f"Dealer's first card: {[computer_cards[0]]}")
    print("-"*55)

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal = input("Type 'hint' to get another card or 'stand' to pass: ").lower()
      clear()
      if user_should_deal == "hint":
        user_cards.append(deal_card())
        user_score = calculate_score(user_cards)
      else:
        is_game_over = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  clear()
  print("-"*55)
  print(f"    Your final hand: {user_cards}, final score: {user_score}")
  print(f"    Dealer's final hand: {computer_cards}, final score: {computer_score}")
  print("-"*55)
  print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
  clear()
  play_game()
