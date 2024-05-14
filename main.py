import random

card_faces = ["Spades", "Hearts", "Diamonds", "Clubs"]
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "King", "Queen", "Jack", "Ace"]
deck = []

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
  wins = 0
  losses = 0
  running = True

  welcome_message = f"""Welcome to this simple Blackjack Game!
You currently have: {wallet}! (If you run out you can take a loan :D)
You have won: {wins} times & lost: {losses} times.
Select one of the optinons below to proceed.
"""
  print(welcome_message)

  while running:
    print("(1): Play a Game")
    print("(2): Take a loan")
    print("(3): Show Stats")
    print("(4): Reset Score")
    print("(5): Exit")
    choice = input("Select a number: ")
    if choice == "1":
      player_hand = []
      house_hand = []
      deck = create_deck(card_faces.copy(), cards.copy())
      random.shuffle(deck)
      print("Shuffling Deck...")

      deal(deck, player_hand)
      deal(deck, player_hand)
      deal(deck, house_hand)
      deal(deck, house_hand)
      busted = False

      print("dealing...")

      while hand_value(player_hand) <21:
        print(f"Your hand is: {player_hand}, {hand_value(player_hand)}")
        decision = input("(1)Hit or (2)Stay: ")
        if decision == "1":
          deal(deck, player_hand)
        
        if decision == "2":
          break

        if hand_value(player_hand) > 21:
          break
          busted = True

      
      while hand_value(house_hand) < 21:
        deal(deck, house_hand)

      if busted:
        print(f"You bust, you had {hand_value(player_hand)}, house had {hand_value(house_hand)}! The House has won this round!")
        losses =+ 1
      
      elif hand_value(player_hand) > hand_value(house_hand) and hand_value(player_hand) <= 21:
        print(f"You've won, you had {hand_value(player_hand)}, house had {hand_value(house_hand)}!")
        wins =+ 1

      elif hand_value(player_hand) == hand_value(house_hand):
        print("Tie")

      else:
        print(f"House wins, you had {hand_value(player_hand)}, house had {hand_value(house_hand)}")
        losses =+ 1
      



      

    elif choice == "2":
      if wallet >= 100:
        print("You're too rich to take a loan!")
      else:
        wallet = 250
        print(wallet)

    elif choice == "3":
      stats = f"""Your stats are as follows:
Wins: {wins}
Losses: {losses}
Current Balance: {wallet}
"""
      print(stats)
    
    elif choice == "4":
      wins = 0
      losses = 0

    elif choice == "5":
      running = False

  else:
    print(f"Thanks for playing, your final stats were. Wins: {wins}, Losses: {losses}")



if __name__ == "__main__":
  launch()