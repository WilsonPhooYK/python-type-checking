import random
from typing import List, Tuple

SUITS = "♠ ♡ ♢ ♣".split()
RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()

Card = Tuple[str, str]
Deck = List[Card]

def create_deck(shuffle: bool = False) -> Deck:
  """Create a new deck

  Args:
      shuffle (bool, optional): If requires shuffle. Defaults to False.
  """
  deck = [(s, r) for r in RANKS for s in SUITS]
  if shuffle:
    random.shuffle(deck)
  return deck

def deal_hands(deck: Deck) -> Tuple[Deck, Deck, Deck, Deck]:
  """Deal the cards in the deck into four hands

  Args:
      deck (list[tuple[str, str]]): Incoming deck
  """
  
  # Jump by 4 in increment
  return (deck[0::4], deck[1::4], deck[2::4], deck[3::4])

def play():
  """Play a 4-player card game
  """
  deck = create_deck(True)
  names = "P1 P2 P3 P4".split()
  # Split into an objects of player: cards
  # { P1:  [('♠', '2'), ('♠', '3')]}
  hands = {n: h for n, h in zip(names, deal_hands(deck))}
  
  for name, cards in hands.items():
    # Print all cards in hand
    card_str = " ".join(f"{s}{r}" for (s, r) in cards)
    print(f"{name}: {card_str}")
    
play()
  
