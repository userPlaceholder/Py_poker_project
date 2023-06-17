
from classes import *

def main():
    main_players_lst = user_input_players()
    main_deck = create_and_shuffle_deck()
    # print(main_players_lst) # For testing
    # print(main_deck.show()) # For testing
    main_players_with_hands = deal(main_players_lst, main_deck)

    evaluate_best_hand(main_players_with_hands)

    winner_or_tied_winners = play(main_players_with_hands)

    if type(winner_or_tied_winners) == Player:
        winner = winner_or_tied_winners
        print(f"""
            The winner is:  * * * {winner.show()} * * *
            The winning hand is:  * {winner.show_hand()} *
            With: {winner.hand_name()}
            """)
    else:
        print("The game is tied between:")
        tied_winners = winner_or_tied_winners
        for player in tied_winners:
            print(f"""
                {player.show()}: {player.show_hand()}, {player.hand_name()}
                """)


def user_input_players():
    players_lst = []
    
    number_of_players = None
    # number_of_players = 7 # For testing

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
    return players_lst


def create_and_shuffle_deck():
    deck = Deck()
    deck.shuffle()
    return deck


def deal(players_lst, shuffled_deck):
    for player in players_lst:
        for num in range(0, 5): # Currently deals 5 cards per player
            player.draw(shuffled_deck)
    
    return players_lst


def evaluate_best_hand(players_with_hands):
    # player_counter = 0 # For testing
    
    for player in players_with_hands:
        
        #player_counter += 1 # For testing
        #print(f"Player counter top: {player_counter}") # For testing

        suits = [card.suit for card in player.hand]
        values = [card.value for card in player.hand]
        # suits = ["\u2663", "\u2663", "\u2663", "\u2663", "\u2663"] # For testing
        # values = [2, 3, 6, 12, 5] # For testing


        def evaluate_flush(suits):
            return suits.count(suits[0]) == len(suits)
        

        def evaluate_straight(values):
            temp_values = values.copy()
            temp_values.sort()
            
            if temp_values == list(range(temp_values[0], temp_values[0] + 5)):
                return True
            
            else:
                if temp_values == [2, 3, 4, 5, 14]:
                    return True
                return False
        
        
        def evaluate_four_of_a_kind(values):
            # print(values) # For testing
            temp_values = values.copy()
            for value in temp_values:
                if temp_values.count(value) == 4:
                    return True
                else:
                    return False
                

        def evaluate_full_house(values):
            temp_values = values.copy()
            three_value = [value for value in temp_values if temp_values.count(value) == 3]
            if len(three_value) == 3:
                for value in three_value:
                    temp_values.remove(value)
                if len(temp_values) == 2 and temp_values[0] == temp_values[1]:
                    return True
                else:
                    return False
            else:
                return False
            

        # Will return True even if full house, but not four-of-a-kind.
        def evaluate_three_of_a_kind(values):
            temp_values = values.copy()
            three_value = [value for value in temp_values if temp_values.count(value) == 3]
            if len(three_value) == 3:
                return True
            else:
                return False
            

        def evaluate_two_pairs(values):
            temp_values = values.copy()
            pairs = [value for value in temp_values if temp_values.count(value) == 2]
            if len(pairs) == 4:
                return True
            else:
                return False
            

        # Will return True even if full house, but not four-of-a-kind.
        def evaluate_one_pair(values):
            temp_values = values.copy()
            # print(values)  # For testing
            pairs = [value for value in temp_values if temp_values.count(value) == 2]
            # print(pairs) # For testing
            if len(pairs) == 2:
                return True
            else:
                return False
            

        flush = evaluate_flush(suits)
        straight = evaluate_straight(values)
        four_of_a_kind = evaluate_four_of_a_kind(values)
        full_house = evaluate_full_house(values) 
        three_of_a_kind = evaluate_three_of_a_kind(values)
        two_pairs = evaluate_two_pairs(values)
        one_pair = evaluate_one_pair(values)

        # Selects best hand according to point system where:
        # 10 pts  Straight flush
        # 9 pts   Four of a kind
        # 8 pts   Full house
        # 7 pts   Flush
        # 6 pts   Straight
        # 5 pts   Three of a kind
        # 4 pts   Two pair
        # 3 pts   Pair
        # 2 pts   Nothing / High card
        
        if straight and flush:
            player.hand_value = 10
        elif four_of_a_kind:
            player.hand_value = 9
        elif full_house:
            player.hand_value = 8
        elif flush:
            player.hand_value = 7
        elif straight:
            player.hand_value = 6
        elif three_of_a_kind:
            player.hand_value = 5
        elif two_pairs:
            player.hand_value = 4
        elif one_pair:
            player.hand_value = 3
        else:
            player.hand_value = 2
        
    
def play(main_players_with_hands):
    top_hand_value = 0
    hand_values = []


    def tie(players, top_hand_value):
        # print(f"Top: {top_hand_value}") # For testing
        tied_players = []
        for player in players:
            # print(f"{player.show()}: {player.show_hand_value()}") # For testing
            if player.show_hand_value() == top_hand_value:
                tied_players.append(player)
        
        return tied_players

    
    for player in main_players_with_hands:
        hand_values.append(player.hand_value)

    hand_values.sort()
    top_hand_value = hand_values[-1]
    
    if hand_values.count(top_hand_value) > 1:
        winners = tie(main_players_with_hands, top_hand_value)
        return winners
    else:
        for player in main_players_with_hands:
            if player.hand_value == top_hand_value:
                return player

    
main()
