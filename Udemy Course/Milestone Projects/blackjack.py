#! python3
# blackjack.py - A game of blackjack between player and AI.
# The simple war game took me 4 hours to make. I don't even want to think how long this is gonna
# take me to program.

import random
import time
import pyinputplus as pyip
import os


SUITS = ("Hearts", "Diamonds", "Spades", "Clubs")
RANKS = ("two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king",)
VALUES = {
"two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
"eight": 8, "nine": 9, "ten": 10, "jack": 10, "queen": 10, "king": 10,
}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = VALUES[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        self.all_deck_cards = []

        for suit in SUITS:
            for rank in RANKS:
                created_card = Card(suit, rank)
                self.all_deck_cards.append(created_card)

    def shuffle_deck(self):
        random.shuffle(self.all_deck_cards)

    def deal_one(self):
        return self.all_deck_cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.player_cards = []
        self.player_values = []
        self.player_balance = 100

    def add_player_cards(self, new_cards, new_values):
        self.player_cards.append(new_cards)
        self.player_values.append(new_values)

    def balance(self, outcome, amount):
        # Outcome will either be win or loss
        if outcome == "w":
            self.player_balance += amount
            print(f"{amount} added to player balance.")
        elif outcome == "l":
            self.player_balance -= amount
            print(f"{amount} has been removed from player balance.")

    def reset_player_hand(self):
        self.player_cards = []
        self.player_values = []

class Dealer:
    def __init__(self):
        self.dealer_cards = []
        self.dealer_values = []
    
    def add_dealer_cards(self, new_cards, new_values):
        self.dealer_cards.append(new_cards)
        self.dealer_values.append(new_values)

    def reset_dealer_hand(self):
        self.dealer_cards = []
        self.dealer_values = []

if __name__ == "__main__":

    # Clear up the terminal
    os.system('cls')

    # Initialize player info
    player_name = pyip.inputStr("Player name: ")
    player = Player(player_name)
    dealer = Dealer()

    # This will be each round of a game. After finishing one game, player can choose to end or play a new round.
    new_round = True
    while new_round:

        print(f"\n{('≡' * 80)}\n")
        # Player makes bet.
        print(f"{player_name}'s Balance: {player.player_balance} Tokens")
        bet_amount = pyip.inputInt("Bet Amount: ")
        if bet_amount > player.player_balance:
            print("You don't have enough tokens.\n")
            continue
        else:
            pass

        # Main loop for the game.
        game_going = True
        while game_going:

            # Since the player has not won yet, this variable will be set to false.
            player_win = False

            # Deck is initialized and randomized with .shuffle_deck()
            # Hands are reset.
            player.reset_player_hand()
            dealer.reset_dealer_hand()
            main_deck = Deck()
            main_deck.shuffle_deck()

            # Two cards are delt to the player, as well as it's corresponding value in a seperate list
            # inside the player class.
            for i in range(2):
                player_card = main_deck.deal_one()
                player.add_player_cards(player_card, player_card.value)

            # Show dealer's first card.
            dealer_card = main_deck.deal_one()
            dealer.add_dealer_cards(dealer_card, dealer_card.value)

            print("\n────────────────────────────\nDealer Hand:\n")
            for dealer_card, dealer_value in zip(dealer.dealer_cards, dealer.dealer_values):
                print(f"Card: {dealer_card} ({dealer_value})")

            dealer_card = main_deck.deal_one()
            dealer.add_dealer_cards(dealer_card, dealer_card.value)

            # Player's turn.
            player_turn = True
            while player_turn:
                print("\n────────────────────────────\nPlayer Turn:\n")

                # Using the zip function, card and value are set using tuple unpacking 
                # and then value is added to the current player's score.
                player_score = 0
                for player_card, player_value in zip(player.player_cards, player.player_values):
                    player_score += player_value
                    print(f"Card: {player_card} ({player_value})")
                print(f"\nTotal Score: {player_score}")

                # The score is checked to see if player won, busted, 
                # or still has a choice to hit/stand.
                if player_score > 21:
                    print('Player busted. Dealer wins.')
                    player_turn = False
                    game_over = True
                    player_win = False
                elif player_score == 21:
                    print('Player got 21. Player wins.')
                    player_turn = False
                    game_over = True
                    player_win = True
                elif player_score < 21:
                    choice = pyip.inputMenu(["hit", "stand"])
                    if choice == "hit":
                        player_card = main_deck.deal_one()
                        player.add_player_cards(player_card, player_card.value)
                        continue
                    elif choice == "stand":
                        game_over = False
                        player_turn = False
            
            # If player already busted, then the game ends without the dealer's turn.
            if game_over:
                if player_win == True:
                    player.balance('w', bet_amount)
                elif player_win == False:
                    player.balance('l', bet_amount)
                break

            # If the previous if statement does not break, it is now the dealer's turn.
            dealer_turn = True
            while dealer_turn:
                print("\n────────────────────────────\nDealer Turn:\n")

                dealer_score = 0
                for dealer_card, dealer_value in zip(dealer.dealer_cards, dealer.dealer_values):
                    print(f"Card: {dealer_card} ({dealer_value})")
                    dealer_score += dealer_value
                print(f'Total Score: {dealer_score}')

                if dealer_score > 21:
                    print('Dealer busted! Player wins.')
                    player_win = True
                    break
                elif dealer_score <= player_score:
                    dealer_card = main_deck.deal_one()
                    dealer.add_dealer_cards(dealer_card, dealer_card.value)
                elif dealer_score > player_score:
                    print("Dealer has beaten player's score. Dealer wins.")
                    player_win = False
                    break

                print('Dealer is thinking...')
                time.sleep(3)

            if player_win == True:
                player.balance('w', bet_amount)
            elif player_win == False:
                player.balance('l', bet_amount)

            # Ends the current round. 
            game_going = False

        # After game is over ask if player wishes to play again.
        play_again = pyip.inputYesNo(f"\n{('─' * 40)}\nPlay Again? (Y/N) ").lower()
        if play_again == "yes":
            continue
        elif play_again == "no":
            print("Thank you for playing blackjack. We hope you enjoyed the games.")
            new_round = False
