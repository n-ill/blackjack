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

    def deal(self): #alternate dealing cards from top of deck to player and dealer until both have 2
        self.player_cards.append(self.deck[0])
        del self.deck[0]
        self.dealer_cards.append(self.deck[0])
        del self.deck[0]
        self.player_cards.append(self.deck[0])
        del self.deck[0]
        self.dealer_cards.append(self.deck[0])
        del self.deck[0]

    def calc_player_total(self):
        self.player_total = 0
        for card in self.player_cards:
            if card[0] == 'J' or card[0] == 'Q' or card[0] == 'K':
                self.player_total += 10
            elif card[0] == 'A':
                if self.player_soft:
                    self.player_total += 11
                else:
                    self.player_total += 1
            else:
                self.player_total += card[0]

    def player_hit(self):
        self.player_cards.append(self.deck[0])
        del self.deck[0]

    def dealer_hit(self):
        self.dealer_cards.append(self.deck[0])
        del self.deck[0]



def main():
    input("Welcome to Blackjack! Press anything to continue...")
    game = Blackjack()
    game.shuffle()
    print('Dealing...')
    time.sleep(1)
    game.deal()
    print(f"Your cards: {game.player_cards[0][0]}{game.player_cards[0][1]}, "
          f"{game.player_cards[1][0]}{game.player_cards[1][1]}")
    print(f"Dealer's cards: {game.dealer_cards[0][0]}{game.dealer_cards[0][1]}, (face down card)")
    game.calc_player_total()
    print(f"Your current total: {game.player_total}")

    while True:
        r = input("hit or stand?")
        if r == 'hit':


if __name__ == "__main__":
    main()