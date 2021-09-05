# war.py - A python recreation of the popular WAR card game.
# Post-program-finished-message - This took me 4 consecutive hours to make. I hate myself for writing
# such a complicated program for such a simple game. I want to die. And no. I will not be 
# explaining more things with comments. I am never coming back to this project. I never want to make something
# with raw Python syntax ever again. 

import random
import time

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king', 'ace')
VALUES = {
    'two': 2, 'three': 3, 'four': 4, 'five': 5,
    'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
    'jack': 11, 'queen': 12, 'king': 13, 'ace': 14
}

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = VALUES[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}' 

class Deck:

    def __init__(self):
        self.all_deck_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_deck_cards.append(created_card)

    def shuffle_deck(self):
        random.shuffle(self.all_deck_cards)

    def deal_one(self):
        return self.all_deck_cards.pop()

class Player:

    def __init__(self, name):
        self.name = name
        self.all_player_cards = []

    def remove_one(self):
        return self.all_player_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_player_cards.extend(new_cards)
        else:
            self.all_player_cards.append(new_cards)

    def check_value(self, card):
        card_words = str(card).split()
        card_words.pop(card_words.index('of'))
        card_words = tuple(card_words)
        rank, suit = card_words
        card_value = Card(suit, rank).value

        return card_value

    def __str__(self):
        return f'Player {self.name} has {len(self.all_player_cards)} cards.'




if __name__ == '__main__':

    new_deck = Deck()
    new_deck.shuffle_deck()

    player1 = Player("Bot1")
    player2 = Player("Bot2")

    for i in range(26):
        card = new_deck.deal_one()
        player1.add_cards(card)

        card = new_deck.deal_one()
        player2.add_cards(card)

    game_going = True
    round = 0
    while game_going:
        print(f'Player 1 Cards: {len(player1.all_player_cards)}')
        print(f'Player 2 Cards: {len(player2.all_player_cards)}')

        player1_card = player1.all_player_cards[0]
        print(f'Player 1 plays {player1_card}')
        player1_card_value = player1.check_value(player1_card)

        player2_card = player2.all_player_cards[0]
        print(f'Player 2 plays {player2_card}')
        player2_card_value = player2.check_value(player2_card)

        if player1_card_value > player2_card_value:

            # Add player 2's card to player 1
            player1.add_cards(player2_card)

            # Put player 1's card at the bottom of deck
            player1.remove_one()
            player1.add_cards(player2_card)

            # Remove player 2's card permanently
            player2.remove_one()
            print('Player 1 wins this round.')

        elif player2_card_value > player1_card_value:

            # Add player 1's card to player 2
            player2.add_cards(player1_card)

            # Put player 2's card at the bottom of deck
            player2.remove_one()
            player2.add_cards(player2_card)

            # Remove player 1's card permanenly
            player1.remove_one()
            print('Player 2 wins this round.')

        else:
            if len(player1.all_player_cards) <= 5:
                print('Player 1 does not have enough cards for war. Player 2 wins.')
                game_going = False
            elif len(player2.all_player_cards) <= 5:
                print('Player 2 does not have enough cards for war. Player 1 wins.')
            else: 
                card_index = 0
                war_going = True
                while war_going is True:
                    print('Both cards have the same value. This means WAR!')


                    # First place 3 cards down for each player

                    # Since this will typically be the same index for both players, another variable
                    # won't be created for the indexes of player2
                    placed_start = player1.all_player_cards.index(player1_card) + 1 + card_index
                    placed_end = player1.all_player_cards.index(player1_card) + 4 + card_index

                    player1_placed = player1.all_player_cards[placed_start:placed_end]
                    player2_placed = player2.all_player_cards[placed_start:placed_end]

                    # Then place final offensive card on top face up
                    offensive_card = player1.all_player_cards.index(player1_card) + 5 + card_index
                    player1_offensive = player1.all_player_cards[offensive_card]
                    player2_offensive = player2.all_player_cards[offensive_card]

                    val1 = player1.check_value(player1_offensive)
                    val2 = player2.check_value(player2_offensive)

                    print(f'Player 1 draws {player1_offensive}')
                    print(f'Player 2 draws {player2_offensive}')

                    if val1 > val2:
                        print(f'Player 1 wins the war.')

                        for card2_placed in player2_placed:
                            player1.all_player_cards.append(card2_placed)
                            print(f"Added {card2_placed} to Player 1's deck.")

                            player2.all_player_cards.pop(player2.all_player_cards.index(card2_placed))

                        war_going = False

                    elif val2 > val1:
                        print('Player 2 wins the war.')

                        for card1_placed in player1_placed:
                            player2.all_player_cards.append(card1_placed)
                            print(f"Added {card1_placed} to Player 2's deck.")

                            player1.all_player_cards.pop(player1.all_player_cards.index(card1_placed))
                        war_going = False
                    elif val1 == val2:
                        print('SPECIAL')
                        card_index += 3
                        continue

        
        # Make sure new cards are used after war is finished.
        try: 
            player1.remove_one()
            player1.add_cards(player1_card)        
    
            player2.remove_one()
            player2.add_cards(player2_card)
        except IndexError:
            if len(player1.all_player_cards) == 1:
                print('Player 2 wins.')
            elif len(player1.all_player_cards) == 1:
                print('Player 1 wins.')

        if len(player1.all_player_cards) == 0:
            print(f'Player 2 wins the game!')
            game_going = False
        elif len(player2.all_player_cards) == 0:
            print(f'Player 1 wins the game!')
            game_going = False
        else:
            pass
    
        print('────────────────────────────')
        round += 1

    print(f'Game took {round} rounds.')

            


        


        

        





