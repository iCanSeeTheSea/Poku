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

def check_for_straight(unique_set):
    unique_set.sort()

    consec_count = 0

    for i in range(0, len(unique_set)-1):
        if unique_set[i] - unique_set[i+1] == 1:
            consec_count += 1

    if consec_count >= 5:
        print(f"{consec_count} card straight")



repeat_count = {}
game = Game(1)
hand = game.show_nums(0)
hand.sort()
hand.reverse()
includes = list(set(hand))
includes.reverse()
repeats = hand.copy()
for num in includes:
    repeats.remove(num)
repeats.sort()
repeats.reverse()

freq = [1 for _ in range(len(includes))]
for num in repeats:
    index = includes.index(num)
    freq[index] += 1
freq.sort()
freq.reverse()


print(hand, includes, repeats, freq)

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

check_for_straight(includes)

for i in range(len(freq)):
    if freq[i] == 5:
        if freq[i+1] == 5:
            print('two quint')
        elif freq[i+1] == 4:
            print('9 card full house')
        else:
            continue
    elif freq[i] == 4:
        if freq[i+1] == 3:
            if freq[i+2] == 2:
                print('fuller house')
            else:
                print('7 card full house')
        elif freq[i+1] == 4:
            print('two quad')
        else:
            continue
    elif freq[i] == 3:
        if freq[i+1] == 3:
            if freq[i+2] == 2 and freq[i+3] == 2:
                print('two full house')
            elif freq[i+2] == 3:
                print('three triple')
            else:
                print('two triple')
        elif freq[i+1] == 2:
            print('5 card full house')
        else:
            continue
    elif freq[i] == 2:
        print('pair')

"""highest frequency:
2:
    - 1-5 pairs

3:
    - 1-3 triples
    - 1-2 full houses

4: 
    - 1-2 quads
    - full house
    - fuller house

5: 
    - 1-2 quints
    - full house

6 - 10:
    - sext -> dix

"""
