import random, time

class Deck:

    def __init__(self):
        self.deck = self.fill_deck()

    def fill_deck(self):
        deck = []
        for suit in ['S', 'C', 'H', 'D']: #spades, clubs, hearts, diamonds
            for num in range(2, 11):
                deck.append([num, suit])
            for face in ['J', 'Q', 'K', 'A']: #jack, queen, king, ace
                deck.append([face, suit])

        return deck

    def shuffle(self):
        random.shuffle(self.deck)

class Blackjack(Deck):

    def __init__(self):
        super().__init__()
        self.player_cards = []
        self.dealer_cards = []

        self.player_total = 0
        self.dealer_total = 0

        self.player_soft = True
        self.dealer_soft = True

        self.player_need_to_calc_ace = False
        self.dealer_need_to_calc_ace = False

        self.player_indexes_of_ace = []
        self.dealer_indexes_of_ace = []

    def deal(self): #alternate dealing cards from top of deck to player and dealer until both have 2
        self.player_cards.append(self.deck[0])
        del self.deck[0]
        self.dealer_cards.append(self.deck[0])
        del self.deck[0]
        self.player_cards.append(self.deck[0])
        del self.deck[0]
        self.dealer_cards.append(self.deck[0])
        del self.deck[0]

    def calc_player_total(self): # aces not being calced correctly
        self.player_total = 0
        for card in self.player_cards:
            if card[0] == 'J' or card[0] == 'Q' or card[0] == 'K':
                self.player_total += 10
            elif card[0] == 'A':
                self.player_need_to_calc_ace = True
                self.player_indexes_of_ace.append(self.player_cards.index(card))
            else:
                self.player_total += card[0]
        if self.player_need_to_calc_ace:
            for index in self.player_indexes_of_ace:
                if self.player_total + 11 > 21:
                    self.player_soft = False
                if self.player_soft:
                    self.player_total += 11
                else:
                    self.player_total += 1

    def calc_dealer_total(self):
        self.dealer_total = 0
        for card in self.dealer_cards:
            if card[0] == 'J' or card[0] == 'Q' or card[0] == 'K':
                self.dealer_total += 10
            elif card[0] == 'A':
                self.dealer_need_to_calc_ace = True
                self.dealer_indexes_of_ace.append(self.dealer_cards.index(card))
            else:
                self.dealer_total += card[0]
        if self.dealer_need_to_calc_ace:
            for index in self.dealer_indexes_of_ace:
                if self.dealer_total + 11 > 21:
                    self.dealer_soft = False
                if self.dealer_soft:
                    self.dealer_total += 11
                else:
                    self.dealer_total += 1

    def player_hit(self):
        self.player_cards.append(self.deck[0])
        del self.deck[0]

    def dealer_hit(self):
        self.dealer_cards.append(self.deck[0])
        del self.deck[0]

    def print_player_cards(self):
        print("Your cards:", end=' ')
        for card in self.player_cards:
            print(f"{card[0]}{card[1]}", end=' ')
        print('')  # newline

    def print_dealer_cards(self):
        print("Dealer's cards:", end=' ')
        for card in self.dealer_cards:
            print(f"{card[0]}{card[1]}", end=' ')
        print('')  # newline

def main():
    input("Welcome to Blackjack! Press anything to continue...")
    game = Blackjack()
    game.shuffle()
    print('Dealing...')
    time.sleep(0.5)
    game.deal()
    game.print_player_cards()
    print(f"Dealer's cards: {game.dealer_cards[0][0]}{game.dealer_cards[0][1]}, (face down card)")
    game.calc_player_total()
    print(f"Your current total: {game.player_total}")

    # player's turn
    while game.player_total < 21:
        r = input("hit or stand?")
        if r == 'hit':
            game.player_hit()
            game.calc_player_total()
            game.print_player_cards()
            print(f"Your current total: {game.player_total}")
        else:
            print(f"Your total: {game.player_total}")
            break

    if game.player_total == 21:
        print("Blackjack! You win!")

    if game.player_total > 21:
        print("Bust! You lose!")

    # dealer's turn
    if game.player_total < 21:
        game.print_dealer_cards()  # reveals face down card
        game.calc_dealer_total()
        print(f"Dealer's total: {game.dealer_total}")

        while game.dealer_total < 17: # dealer must hit until 17, at 17 or higher must stay
            print("Dealer hit...")
            game.dealer_hit()
            game.calc_dealer_total()
            game.print_dealer_cards()
            print(f"Dealer's total: {game.dealer_total}")

        if game.dealer_total == 21:
            print("Dealer blackjack! You lose!")
        elif game.dealer_total > 21:
            print("Dealer bust! You win!")
        else:
            # print who wins
            if game.player_total > game.dealer_total:
                print("You won!")
            elif game.player_total == game.dealer_total:
                print("Tie!")
            else:
                print("Dealer wins!")

if __name__ == "__main__":
    main()