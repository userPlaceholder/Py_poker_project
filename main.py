# A poker-type game created as part of a Python course
# with the purpose to utilise classes 

from classes import *


# bob = Player("Bob")

#for i in range(0, 5):
#    bob.draw(deck)

#bob.show_hand()

# FUNCTION SPLIT:
# X Main, calls functions
# X Input, takes input, returns list of players
# X Create deck, creates and shuffles deck
# X Deal, assign player hands
# * Calculate, calculate best hand for each player
# Itertools: https://www.geeksforgeeks.org/itertools-combinations-module-python-print-possible-combinations/
# * Play, plays best hand

def main():
    main_players_lst = user_input_players()
    main_deck = create_and_shuffle_deck()
    #print(main_players_lst) # For testing
    #print(main_deck.show()) # For testing
    main_players_with_hands = deal(main_players_lst, main_deck)
    
    # For testing:
    #for player in main_players_lst:
    #    print("X")
    #    print(player.show_hand())
    #    print("Y")

    players_top_hands = evaluate_best_hand(main_players_with_hands)



def user_input_players():
    players_lst = []
    
    # number_of_players = None
    number_of_players = 7 # Change back!!!

    while number_of_players == None:
        user_input = input("Select number of players (1-7): ")
        try:
            int(user_input)
        except ValueError:
            print("You must input an integer between 1-7.")
            continue
        else:
            if int(user_input) < 1 or int(user_input) > 7:
                print("You must input an integer between 1-7.")
                continue

        number_of_players = int(user_input)

    for item in range(1, number_of_players + 1):
        player = Player("Player " + (str(len(players_lst) + 1)))
        #print(player.show_hand())
        players_lst.append(player)
        #print(player) # For testing
    #for item in players_lst:
    #    print(item.show_hand())
    return players_lst

def create_and_shuffle_deck():
    deck = Deck()
    deck.shuffle()
    return deck

def deal(players_lst, shuffled_deck):
    for player in players_lst:
        for num in range(0, 5): # Currently deals 5 cards per player
            player.draw(shuffled_deck)
    # For testing:
    #for player in players_lst:
    #    print("Start")
    #    player.show_hand()
    #    print("Stop")
    
    return players_lst

def evaluate_best_hand(players_with_hands):
    #for player in players_with_hands:
    #for card in player.hand:
    #    print(card)
    #print("END")
    
    for player in players_with_hands:
        # Keeps track of player numbers: (Necessary?) 
        player_counter = 0
        player_counter += 1

        def evaluate_flush():
            # suits = ["\u2663", "\u2663", "\u2663", "\u2663", "\u2663"] # For testing
            suits = [card.suit for card in player.hand]
            return suits.count(suits[0]) == len(suits)
        
        def evaluate_straight():
            values = [card.value for card in player.hand]
            # values = [10, 8, 9, 11, 7] # For testing
            values.sort()
            # print(values) # For testing
            # print(list(range(values[0], values[0] + 5))) # For testing

            if values == list(range(values[0], values[0] + 5)):
                return True
            
            else:
                if values == [2, 3, 4, 5, 14]:
                    return True
                return False
        
        def evaluate_four_of_a_kind():
            pass
    
    flush = evaluate_flush() # Working!
    straight = evaluate_straight() # Working!
    four = evaluate_four_of_a_kind()
    print(four)
    

    # Checks:
    # O Straight flush
    # O Four of a kind
    # O Full house 
    # X Flush
    # X Straight
    # O Three of a kind
    # O Two pairs
    # O Pair
    # O High card

            






main()
