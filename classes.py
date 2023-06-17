
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
        if self.value > 10:
            if self.value == 11:
                return f"J{self.suit}"
            elif self.value == 12:
                return f"Q{self.suit}"
            elif self.value == 13:
                return f"K{self.suit}"
            elif self.value == 14:
                return f"A{self.suit}"
        else:
            return f"{self.value}{self.suit}"
    
    def show(self):
        print(f"{self.value} of {self.suit}")


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.hand_value = 0

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
            hand_str += str(card) + "  "
        return hand_str.rstrip()
    
    def show_hand_value(self):
        return self.hand_value
    
    def hand_name(self):
        if self.hand_value == 0:
            return "No hand has been dealt!"
        elif self.hand_value == 10:
            return "Straight flush"
        elif self.hand_value == 9:
            return "Four-of-a-kind"
        elif self.hand_value == 8:
            return "Full house"
        elif self.hand_value == 7:
            return "Flush"
        elif self.hand_value == 6:
            return "Straight"
        elif self.hand_value == 5:
            return "Three-of-a-kind"
        elif self.hand_value == 4:
            return "Two pairs"
        elif self.hand_value == 3:
            return "One pair"
        elif self.hand_value == 2:
            return "High card"
        else:
            return "Invalid hand value"