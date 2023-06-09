import random

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def __str__(self):
        return "A deck of cards. Use .show() method to print all cards in deck."

    def build(self):
        # Clubs, Diamonds, Hearts, Spades in aphabetical order:
        for suit in ["\u2663", "\u2666", "\u2665", "\u2660"]:
            for value in range(2, 15):
                self.cards.append(Card(suit, value))

    def show(self):
        for card in self.cards:
            card.show()
    
    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"
    
    def show(self):
        print(f"{self.value} of {self.suit}")


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def __str__(self):
        return f"String representation of player: {self.name}"
    
    def show(self):
        return f"{self.name}"
    
    def draw(self, deck):
        self.hand.append(deck.draw_card())
        return self
        
    def show_hand(self):
        hand_str = ""
        for card in self.hand:
            hand_str += str(card) + "\n"
        return hand_str.rstrip()