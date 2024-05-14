import random

card_faces = ["Spades", "Hearts", "Diamonds", "Clubs"]
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "King", "Queen", "Jack", "Ace"]
deck = []
player_hand = []
house_hand = []

def create_deck(card_faces, cards):
  deck = []
  for face in card_faces:
    for card in cards:
      deck.append(f"{card} of {face}")
  return deck

# Dealing Cards
def deal(deck, hand):
  if not deck:
    raise ValueError("Deck is Empty.")
  
  drawn_card = deck.pop()
  hand.append(drawn_card)

# Calculating
def hand_value(hand):
  value = 0
  aces = 0

  for card in hand:
    rank = card.split()[0]

    if rank in ["King", "Queen", "Jack"]:
      value += 10
    elif rank == "Ace":
      value += 11
      aces += 1
    else:
      value += int(rank)

  while value > 21 and aces > 0:
    value -= 10
    aces -= 1

  return value


# Make a welcome message, then select between playing, loan, display money left, win/loss ratio.
def launch():
  wallet = 250

