# testing methods for hand scoring and recognition

from dataclasses import dataclass
import random

num_to_colour = {
    0: "red",
    1: "green",
    2: "blue",
    3: "yellow"
}


@dataclass(eq=True, frozen=True)
class Card:
    __id: int
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
        self._cards = set()
        self.size = len(self._cards)

    def show_cards(self):
        shown = []
        for card in self._cards:
            shown.append(card.number)
        return shown

    def add_card(self, card):
        self._cards.add(card)


class Deck(CardGroup):
    def __init__(self):
        super().__init__()

        for i in range(0, 160):
            colour = num_to_colour[i // 40]
            self._cards.add(Card(i, i % 10, colour))

    def get_random_card(self):
        card = random.choice(tuple(self._cards))
        self._cards.remove(card)
        return card

    def add_card(self, card):
        return


class Game:
    def __init__(self, players):
        self._table = CardGroup()
        self._deck = Deck()
        self._hands = []

        for _ in range(players):
            self._hands.append(CardGroup())

        for _ in range(2):
            for hand in self._hands:
                hand.add_card(self._deck.get_random_card())

        for _ in range(5):
            self._table.add_card(self._deck.get_random_card())

    def show_hand(self, index):
        shown = self._table.show_cards()
        return shown + self._hands[index].show_cards()


game = Game(1)
for i in range(1):
    print(game.show_hand(i))


