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

        for _ in range(5):
            for hand in self._hands:
                hand.add_card(self._deck.get_random_card())

        for _ in range(10):
            self._table.add_card(self._deck.get_random_card())

    def show_nums(self, index):
        shown = self._table.show_cards()
        return shown + self._hands[index].show_cards()


# pair
# two pair
# three of a kind
# straight
# full house
# four of a kind

def check_for_straight(set):
    s_list = list(set)
    s_list.sort()
    hands = []
    for n in range(5, len(s_list)+1):
        up_to = n
        hands.append(s_list[n-5:up_to])

    for h in hands:
        for i in range(0, len(h)-1):
            if h[i+1] - h[i] > 1:
                break
        else:
            return True

    return False


repeat_count = {}
game = Game(1)
hand = game.show_nums(0)
includes = set(hand)
repeats = hand.copy()
for num in includes:
    repeats.remove(num)
print(hand, includes, repeats)


# if difference == 0:
#     if check_for_straight(includes):
#         print('straight')
# elif difference == 1:
#     if check_for_straight(includes):
#         print('straight')
#     else:
#         print('pair')
# elif difference == 2:
#     if check_for_straight(includes):
#         print('straight')
#     elif len(set(repeats)) == 1:
#         print('three of a kind')
#     else:
#         print('two pair')
# elif difference == 3:
#     if len(set(repeats)) == 1:
#         print('four of a kind')
#     elif len(set(repeats)) == 2:
#         print('full house')
#     else:
#         print('two pair')
# elif difference == 4:
#     if len(set(repeats)) <= 2:
#         print('four of a kind')
#     else:
#         print('full house')
# else:
#     print('four of a kind')

"""
straight
pair
triple
two pair 
quad
quint
full house 
sext
three pair 
two triple 
sept
7 card full house
oct
four pair 
two quad 
nonce
three triple 
fuller house 
9 card full house 
dix
five pair 
two quint 
two full house 
"""

