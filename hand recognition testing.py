# testing methods for hand scoring and recognition

from dataclasses import dataclass
from random import randint

num_to_colour = {
    0: "red",
    1: "green",
    2: "blue",
    3: "yellow"
}


@dataclass
class Card:
    __number: int
    __colour: str

    @property
    def number(self):
        return self.__number

    @property
    def colour(self):
        return self.__colour

    def show(self):
        return f"{self.__colour} {self.__number}"


class CardGroup:
    def __init__(self):
        self._cards = []
        self.size = len(self._cards)


class Deck(CardGroup):
    def __init__(self):
        super().__init__()

        for i in range(0, 160):
            colour = num_to_colour[i // 40]
            self._cards.append(Card(i % 10, colour))

    def getRandomCard(self):
        index = randint(0, len(self._cards)-1)
        return self._cards.pop(index)


class Hand(CardGroup):
    def __int__(self):
        super().__init__()
        self._score = 0

    def addCard(self, card):
        self._cards.append(card)

    def showHand(self):
        shownHand = []
        for card in self._cards:
            shownHand.append(card.show())
        return shownHand


deck = Deck()
hand = Hand()
for i in range(0, 5):
    hand.addCard(deck.getRandomCard())

print(hand.showHand())


