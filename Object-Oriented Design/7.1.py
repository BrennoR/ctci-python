# Deck of Cards
# TODO: Improve aces functionality
import random


class Card:

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.available = True

    def is_available(self):
        return self.is_available()


class Deck:

    def __init__(self):
        self.deck = []
        self.out_deck = []
        for suit in ['Spades', 'Heart', 'Diamond', 'Clubs']:
            for value in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 'A']:
                self.deck.append(Card(value, suit))
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.deck)

    def draw(self):
        card = self.deck.pop()
        self.out_deck.append(card)
        return card

    def is_empty(self):
        return self.deck == []

    def rebuild_deck(self):
        total_deck = self.deck + self.out_deck
        random.shuffle(total_deck)
        self.out_deck = []
        self.deck = total_deck


class Blackjack(Deck):

    def play(self):
        value = 0
        aces = 0
        while True:
            if value >= 21:
                break
            action = input('Please enter an action [D - Draw, S - Stop]:')
            if action == 'D':
                card = self.draw()
                if card.value == 'A':
                    aces = 1
                    if value + 11 <= 21:
                        value += 11
                    else:
                        value += 1
                        aces -= 1
                else:
                    value += card.value
                print('Value: {}, Aces: {}'.format(value, aces))
            elif action == 'S':
                break

        if value == 21:
            print("21! Congrats you've won!")
            return

        while aces > 0 and value > 21:
            value -= 10
            aces -= 1

        if value > 21:
            print("Final Value: {}, You've lost!".format(value))
            return

        print("Final Value: {}".format(value))
        return


if __name__ == '__main__':

    blackjack = Blackjack()
    blackjack.play()
