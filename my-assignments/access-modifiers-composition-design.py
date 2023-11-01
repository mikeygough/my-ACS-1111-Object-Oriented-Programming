import random

#In this example we will walk through how different access modifiers are indicated in Python
class Snake:
  def __init__(self, name, color, type):
    #public property
    self.name = name

    #protected
    self._color = color

    #private
    self.__type = type

  def example1(self):
    print("I eat rodents! (This is public)")

  def _example2(self):
    print("I like to slither in the sand (This is protected)")
    self.__example3()

  def __example3(self):
    print("I like to curl up on a hot rock! (This is private)")

# Make a snek caled albert
albert = Snake("Albert", "yellow", "Python")

# Look at each line below. Predict the output 
# by examining the class above. Then uncomment 
# the line and run the code: 

# albert.__example3() --> AttributeError: 'Snake' object has no attribute '__example3'
# albert.example1() --> I eat rodents! (This is public)
# albert._example2() --> I like to slither in the sand (This is protected)
# print(albert.name) --> Albert
# print(albert._color) --> yellow
# print(albert._Snake__type) --> Python
# print( dir(albert) ) --> ['_Snake__example3', '_Snake__type', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_color', '_example2', 'example1', 'name']

# Make a class that creates an instance of yourself! 
# Your class will have some public, protected, and 
# private attributes. 

#TODO: Create a class that desribes you! Give your class three attributes
class Human:
  def __init__(self, name: str, organ_donor: bool, weight: int):
    #public property
    self.name = name

    #protected
    self._organ_donor = organ_donor

    #private
    self.__weight = weight

  def example1(self):
    print(f"Hello, my name is {self.name}")

  def _example2(self):
    print("I may or may not be an organ donor (This is protected)")

  def __example3(self):
    print(f"My weight is {self.__weight} (This is private)")


class Card():
    def __init__(self, suit, value, color, deck):
        self.suit = suit
        self.value = value
        self.color = color
        self.deck = deck
        
    def show(self):
        print(f"{self.value} {self.suit}")
        
    def discard(self):
        self.deck.cards.remove(self)
        self.deck.discard(self)
        
class Deck():
    def __init__(self, cards=[], discard_pile=[]):
        self.cards = cards
        self.discard_pile = discard_pile
        
    def add_card(self, card):
        self.cards.append(card)
        
    def add_cards(self, *cards):
        for card in cards:
            self.cards.append(card)
        
    def shuffle(self):
        random.shuffle(self.cards)
        
    def display_deck(self):
        for card in self.cards:
            card.show()
            
    def draw(self):
        if len(self.cards) > 0:
            return self.cards.pop(0)
        else:
            print("No cards left to draw!")
            
    def draw_hand(self, num_of_cards):
        cards = []
        for i in range(num_of_cards):
            if len(self.cards) > 0:
                cards.append(self.draw())
            else: print("No cards left to draw!")
        return Hand(deck=self, cards=cards)
            
    def discard(self, card):
        self.discard_pile.append(card)
        
    def display_discard_pile(self):
        for card in self.discard_pile:
            card.show()
            
class Hand():
    def __init__(self, deck, cards=[]):
        self.deck = deck
        self.cards = cards
        
    def display_hand(self):
        for card in self.cards:
            card.show()
            
    def draw(self):
        pass
        
# create deck
deck = Deck()

# create cards
ace_spades = Card("♠", "ace", "black", deck=deck)
ace_clubs = Card("♣", "ace", "black", deck=deck)
ace_hearts = Card("♥", "ace", "red", deck=deck)
ace_diamonds = Card("♦", "ace", "red", deck=deck)

print("DECK")
deck.add_cards(ace_spades, ace_clubs, ace_hearts, ace_diamonds)
deck.display_deck()
deck.shuffle()
print("DECK AFTER SHUFFLE")
deck.display_deck()

print("2 CARD HAND")
your_hand = deck.draw_hand(2)
your_hand.display_hand()

print("DECK BEFORE DISCARD")
deck.display_deck()
print("DECK AFTER DISCARDING 1 CARD")
ace_spades.discard()
deck.display_deck()
print("DISCARD PILE")
deck.display_discard_pile()

# magic trick...
# print("Pick a card, any card... And don't show it to me!")
# your_card = deck.draw()
# print(f"\nI will now guess the card your drew... Was it, the {your_card.value} of {your_card.suit} !?")

