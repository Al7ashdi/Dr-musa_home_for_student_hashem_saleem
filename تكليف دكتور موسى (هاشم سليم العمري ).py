import random

class Card:
    def __init__(self):
        self.cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    def deal_card(self):
        return random.choice(self.cards)

class Player:
    def __init__(self):
        self.cards = []
        self.score = 0

    def calculate_score(self):
        if sum(self.cards) == 21 and len(self.cards) == 2:
            return 0
        if 11 in self.cards and sum(self.cards) > 21:
            self.cards.remove(11)
            self.cards.append(1)
        self.score = sum(self.cards)
        return self.score

class BlackjackGame:
    def __init__(self):
        self.player = Player()
        self.computer = Player()
        self.deck = Card()

    def initial_deal(self):
        for _ in range(2):
            self.player.cards.append(self.deck.deal_card())
            self.computer.cards.append(self.deck.deal_card())
        self.player.calculate_score()
        self.computer.calculate_score()

    def display_hands(self):
        print(f"Your cards: {self.player.cards}, current score: {self.player.score}")
        print(f"Computer's cards: {self.computer.cards}, current score: {self.computer.score}")

    def play_game(self):
        self.initial_deal()
        is_game_over = False

        while not is_game_over:
            self.display_hands()

            if self.player.score == 0 or self.computer.score == 0 or self.player.score > 21:
                is_game_over = True
            else:
                should_continue = input("Type 'y' to get another card, type 'n' to pass: ")
                if should_continue == 'y':
                    self.player.cards.append(self.deck.deal_card())
                    self.player.calculate_score()
                else:
                    is_game_over = True

        while self.computer.score != 0 and self.computer.score < 17:
            self.computer.cards.append(self.deck.deal_card())
            self.computer.calculate_score()

        self.display_hands()

        if self.player.score > 21:
            print("You went over. You lose.")
        elif self.computer.score > 21:
            print("Computer went over. You win!")
        elif self.player.score == self.computer.score:
            print("It's a draw.")
        elif self.player.score == 0:
            print("You win with a Blackjack!")
        elif self.computer.score == 0:
            print("Computer wins with a Blackjack!")
        elif self.player.score > self.computer.score:
            print("You win!")
        else:
            print("You lose.")

def main():
    game = BlackjackGame()
    game.play_game()

if __name__ == "__main__":
    main()