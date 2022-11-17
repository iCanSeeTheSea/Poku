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

    consecutive_count = 0
    for i in range(0, len(unique_set)-1):
        if unique_set[i+1] - unique_set[i] == 1:
            consecutive_count += 1
        elif consecutive_count < 5:
            consecutive_count = 0

    if consecutive_count >= 5:
        return consecutive_count
    return 0


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


cards_used = 0
combinations = []
pairs = 0
for i in range(len(freq)):
    if freq[i] >= 5:
        if freq[i+1] >= 5:
            combinations.append([10, 'two quint'])
        else:
            combinations.append([5, 'quint'])
        if freq[i+1] >= 4:
            combinations.append([9, '9 card full house'])
    if freq[i] >= 4:
        if freq[i+1] >= 3:
            if freq[i+2] >= 2:
                combinations.append([9, 'fuller house'])
            else:
                combinations.append([7, '7 card full house'])
        if freq[i+1] >= 4:
            combinations.append([8, 'two quad'])
        else:
            combinations.append([4, 'quad'])
    if freq[i] >= 3:
        if freq[i+1] >= 3:
            if freq[i+2] >= 2 and freq[i+3] >= 2:
                combinations.append([10, 'two full house'])
            elif freq[i+2] >= 3:
                combinations.append([9, 'three triple'])
            else:
                combinations.append([6, 'two triple'])
        else:
            combinations.append([3, 'triple'])
        if freq[i+1] >= 2:
            combinations.append([5, '5 card full house'])
    if freq[i] >= 2:
        pairs += 1
        if pairs > 5:
            pairs = 5

if pairs:
    combinations.append([pairs*2, f"{pairs} pair"])


straight_cards = check_for_straight(includes)
if straight_cards:
    combinations.append([straight_cards, f"{straight_cards} card straight"])

print(combinations)


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
