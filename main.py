import random

def calculate_score(score):
  if score == [11,10] or score == [10,11]:
    print("Black Jack")
  score_sum = sum(score)
  return score_sum


def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

user_cards = []
computer_cards = []

for _ in range(2):
  user_cards.append(deal_card())
  computer_cards.append(deal_card())

user_result = calculate_score(user_cards)
computer_result = calculate_score(computer_cards)

print(f"Cards: {user_cards} Sum: {user_result}, Dealer cards:  {computer_cards} Sum: {computer_result}")