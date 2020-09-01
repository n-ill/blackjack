import blackjack
import pygame

class button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('timesnewroman', 24)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (
            self.x + int(self.width / 2 - text.get_width() / 2), self.y + int(self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False


def draw_player_cards(a_screen, a_game):
    player_card_offset = 0
    for card in game.player_cards:
        card_image = card_images[f"{card[0]}{card[1]}"]
        card_resize = pygame.transform.scale(card_image, (125, 175))
        screen.blit(card_resize, (435 + player_card_offset, 425))
        player_card_offset += 25

def draw_dealer_cards(a_screen, a_game):
    dealer_card_offset = 0
    for card in game.dealer_cards:
        card_image = card_images[f"{card[0]}{card[1]}"]
        card_resize = pygame.transform.scale(card_image, (125, 175))
        screen.blit(card_resize, (435 + dealer_card_offset, 5))
        dealer_card_offset += 25

def draw_text(a_text, a_screen, x, y, a_width):
    font = pygame.font.SysFont('timesnewroman', 22)
    text = font.render(a_text, 1, (0,0,0))
    pygame.draw.rect(a_screen, (0, 0, 0), pygame.Rect(x - 2, y - 2, 34, 34))
    pygame.draw.rect(a_screen, (255,255,255), pygame.Rect(x,y, a_width,30))
    a_screen.blit(text, (x,y))

def draw_inital_dealer_cards(screen, game):
    dealer_card_offset = 0

    card_image = card_images[
        f"{game.dealer_cards[0][0]}{game.dealer_cards[0][1]}"]  # first dealer card - second faced down
    card_resize = pygame.transform.scale(card_image, (125, 175))
    screen.blit(card_resize, (435 + dealer_card_offset, 5))
    dealer_card_offset += 25

    card_back = pygame.image.load('card_back.png').convert_alpha()
    card_back_resize = pygame.transform.scale(card_back, (125, 175))
    screen.blit(card_back_resize, (435 + dealer_card_offset, 5))
    dealer_card_offset += 25

WIDTH = 999
HEIGHT = 679

card_images = {}

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Blackjack')
clock = pygame.time.Clock()

background = pygame.image.load('blackjack_table.jpeg')

for suit in ['S', 'C', 'H', 'D']:  # spades, clubs, hearts, diamonds
    for num in range(2, 11):
        card_images[f"{num}{suit}"] = pygame.image.load(f'./card_images/{num}{suit}.png')
    for face in ['J', 'Q', 'K', 'A']:  # jack, queen, king, ace
        card_images[f"{face}{suit}"] = pygame.image.load(f'./card_images/{face}{suit}.png')

button_deal = button((0, 255, 255), 800, 600, 50, 50, 'Deal')
button_hit = button((0, 255, 0), 200, 600, 50, 50, 'Hit')
button_stand = button((255, 0, 0), 275, 600, 50, 50, 'Stand')
button_play_again = button((200, 200, 200), 800, 500, 100, 50, 'Play Again')

game_over = False
while not game_over:
    game = blackjack.Blackjack()
    game.shuffle()

    has_dealt = False
    players_turn = True
    running = True
    done = False

    while running:
        screen.blit(background, (0, 0))

        if not has_dealt:
            button_deal.draw(screen, (0,0,0))

        if has_dealt:
            if game.player_total == 21:
                draw_text('Blackjack!', screen, 350, 475, 75)
                draw_text('You Win!', screen, int(WIDTH/2) - 25, int(HEIGHT/2), 100)
            if game.player_total > 21:
                draw_text('Bust!', screen, 350, 475, 50)
                draw_text('You Lose!', screen, int(WIDTH/2) - 25, int(HEIGHT/2), 100)

            draw_player_cards(screen, game)
            draw_text(str(game.player_total), screen, 500, 625, 30)  # player's score

            if players_turn:
                button_hit.draw(screen, (0, 0, 0))
                button_stand.draw(screen, (0, 0, 0))
                draw_inital_dealer_cards(screen, game)
            else:  # dealer's turn
                draw_dealer_cards(screen, game)
                game.calc_dealer_total()
                draw_text(str(game.dealer_total), screen, 500, 205, 30)  # dealer's score
                if game.dealer_total < 17:
                    game.dealer_hit()
                else:
                    done = True

            if game.dealer_total == 21:
                draw_text('Blackjack!', screen, 350, 50, 75)
                draw_text('You Lose!', screen, int(WIDTH/2) - 25, int(HEIGHT/2), 100)
            if game.dealer_total > 21:
                draw_text('Bust!', screen, 350, 50, 50)
                draw_text('You Win!', screen, int(WIDTH/2) - 25, int(HEIGHT/2), 100)
            if done:
                if game.player_total == game.dealer_total:
                    draw_text('Tie!', screen, int(WIDTH / 2) - 25, int(HEIGHT / 2), 50)
                elif game.player_total > game.dealer_total:
                    draw_text('You Win!', screen, int(WIDTH / 2) - 25, int(HEIGHT / 2), 100)
                else:
                    draw_text('You Lose!', screen, int(WIDTH / 2) - 25, int(HEIGHT / 2), 100)

                button_play_again.draw(screen, (0, 0, 0))

        # events
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                running = False
                game_over = True

            # clicking buttons
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_deal.isOver(pos):
                    game.deal()
                    game.calc_player_total()
                    has_dealt = True
                if button_hit.isOver(pos):
                    game.player_hit()
                    game.calc_player_total()
                if button_stand.isOver(pos):
                    players_turn = False
                if button_play_again.isOver(pos):
                    running = False

            # hovering buttons
            if event.type == pygame.MOUSEMOTION:
                if button_deal.isOver(pos):
                    button_deal.color = (0,175,175)
                else:
                    button_deal.color = (0, 255, 255)

                if button_hit.isOver(pos):
                    button_hit.color = (0,175,0)
                else:
                    button_hit.color = (0, 255, 0)

                if button_stand.isOver(pos):
                    button_stand.color = (175,0,0)
                else:
                    button_stand.color = (255, 0, 0)

                if button_play_again.isOver(pos):
                    button_play_again.color = (120, 120, 120)
                else:
                    button_play_again.color = (200, 200, 200)

        pygame.display.flip()
        clock.tick(60)

pygame.quit()