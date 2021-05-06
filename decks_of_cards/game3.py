import random
import sys
from typing import Optional, Iterator, List

class Card:
  SUITS = "♠ ♡ ♢ ♣".split()
  RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()
  
  def __init__(self, suit: str, rank: str) -> None:
    self.suit = suit
    self.rank = rank
  
  def __repr__(self) -> str:
      return f"{self.suit}{self.rank}"
    
class Deck:
  def __init__(self, cards: List[Card]) -> None:
    self.cards = cards
    
  # Static method
  @classmethod
  def create(cls, shuffle: bool = False) -> "Deck":
    """Create a new deck

    Args:
        shuffle (bool, optional): If requires shuffle. Defaults to False.
    """
    cards = [Card(s, r) for r in Card.RANKS for s in Card.SUITS]
    if shuffle:
      random.shuffle(cards)
    return cls(cards)
  
  def deal(self, num_hands: int) -> Iterator["Deck"]:
    """Deal the cards in the deck into a number of hands

    Args:
        num_hands int: Number of hands
    """
    cls = self.__class__
    return (cls(self.cards[i::num_hands]) for i in range(num_hands))
  
class Player:
  def __init__(self, name: str, hand: Deck) -> None:
    self.name = name
    self.hand = hand
    
  def play_card(self) -> Card:
    """Play a card from the player's hand
    """
    card = random.choice(self.hand.cards)
    self.hand.cards.remove(card)
    print(f"{self.name}: {card!r:<3}  ", end="")
    return card
  
class Game:
  def __init__(self, *names: str) -> None:
    """Set up the deck and deal cards to 4 players
    """
    deck = Deck.create(True)
    self.names = (list(names) + "P1 P2 P3 P4".split())[:4]
    self.hands = {
      n: Player(n, h) for n, h in zip(self.names, deck.deal(4))
    }
    
  def play(self):
    """Play a card game
    """
    start_player: str = random.choice(self.names)
    turn_order = self.player_order(start_player)
    
    # Play cards from each player's hand until empty
    while self.hands[start_player].hand.cards:
      for name in turn_order:
        self.hands[name].play_card()
      print()
      
  def player_order(self, start: Optional[str] = None):
    """Rotate player order so that start goes first

    Args:
        start (str, optional): Start player name. Defaults to None.
    """
    if start is None:
        start = random.choice(self.names)
    start_idx = self.names.index(start)
    return self.names[start_idx:] + self.names[:start_idx]
    
player_names = sys.argv[1:]
game = Game(*player_names)
game.play()
