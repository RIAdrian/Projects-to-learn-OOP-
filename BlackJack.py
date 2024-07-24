import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = self.determine_value()

    def determine_value(self):
        if self.rank in ['J', 'Q', 'K']:
            return 10
        elif self.rank == 'A':
            return 11 
        else:
            return int(self.rank)

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

class Pack:
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    def __init__(self):
        self.cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

    def __repr__(self):
        return f"Pack of {len(self.cards)} cards"

class Player:
    def __init__(self, name, pack):
        self.name = name
        self.hand = []
        self.pack = pack
        self.bet = 0
        self.total_money = 1000 

    def draw_card(self):
        card = self.pack.deal_card()
        self.hand.append(card)
        return card

    def show_hand(self):
        return f"{self.name}'s hand: {self.hand}"

    def calculate_hand_value(self):
        value = sum(card.value for card in self.hand)
        # Adjust for Aces
        num_aces = sum(1 for card in self.hand if card.rank == 'A')
        while value > 21 and num_aces:
            value -= 10
            num_aces -= 1
        return value

    def double_bet(self):
        self.bet *= 2

    def __repr__(self):
        return f"Player({self.name}, {self.total_money})"

class Dealer(Player):
    def __init__(self, pack):
        super().__init__("Dealer", pack)

    def play(self):
        while self.calculate_hand_value() < 17:
            self.draw_card()
        return self.show_hand()

class Game:
    def __init__(self):
        self.pack = Pack()
        self.player = Player("User", self.pack)
        self.dealer = Dealer(self.pack)

    def start(self):
        print("Welcome to Blackjack!")
        self.player.bet = int(input(f"{self.player.name}, how much do you want to bet: "))
        
        self.player.draw_card()
        self.player.draw_card()
        self.dealer.draw_card()
        self.dealer.draw_card()

        print(self.player.show_hand())
        print(f"Dealer's visible card: {self.dealer.hand[0]}")

        self.player_turn()
        self.dealer_turn()
        self.check_winner()

    def player_turn(self):
        while True:
            choice = input("What action? (hit/stand/double): ").lower()
            if choice == 'hit':
                self.player.draw_card()
                print(self.player.show_hand())
                if self.player.calculate_hand_value() > 21:
                    print("You lost! Score over >21.")
                    return
            elif choice == 'stand':
                break
            elif choice == 'double':
                self.player.double_bet()
                self.player.draw_card()
                print(self.player.show_hand())
                if self.player.calculate_hand_value() > 21:
                    print("You lost! Score over >21.")
                return
            else:
                print("Invalid Option")

    def dealer_turn(self):
        print(self.dealer.play())
        if self.dealer.calculate_hand_value() > 21:
            print("Dealer lost! Score over >21. ")
        
    def check_winner(self):
        player_value = self.player.calculate_hand_value()
        dealer_value = self.dealer.calculate_hand_value()

        if player_value > 21:
            print("Dealer won! ")
        elif dealer_value > 21 or player_value > dealer_value:
            print(f"Congrats, {self.player.name}! You won!")
        elif player_value < dealer_value:
            print("Dealer Won!")
        else:
            print("Draw!")


game = Game()
game.start()
