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
        self._cards = [[] for _ in range(10)]
        self.size = len(self._cards)

    def show_cards(self):
        shown = []
        for number in self._cards:
            for card in number:
                shown.append(card)
        return shown

    def add_card(self, card):
        self._cards[card.number].append(card)
        self.size += 1

    def get_card_list(self):
        return self._cards


class Deck(CardGroup):
    def __init__(self):
        super().__init__()
        self._cards = []

        for i in range(0, 160):
            colour = num_to_colour[i // 40]
            self._cards.append(Card(i, i % 10, colour))

    def get_random_card(self):
        card = random.choice(self._cards)
        self._cards.remove(card)
        return card

    def add_card(self, card):
        pass


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

    def get_full_hand(self, index):
        hand = self._hands[index].show_cards()
        full_hand = self._table
        for card in hand:
            full_hand.add_card(card)
        return full_hand

    def show_hand(self, index):
        full_hand = self.get_full_hand(index)
        return full_hand.show_cards()

    def get_unique_numbers_and_frequencies(self, index):
        full_hand = self.get_full_hand(index)
        unique_nums = []
        freq = []
        for number in full_hand.get_card_list():
            if number:
                unique_nums.append(number[0].number)
                freq.append(len(number))
        return unique_nums, freq


def check_for_straight(unique_set):
    unique_set.sort()

    consecutive_count = 1
    for i in range(0, len(unique_set)-1):
        if unique_set[i+1] - unique_set[i] == 1:
            consecutive_count += 1
        elif consecutive_count < 5:
            consecutive_count = 1

    if consecutive_count >= 5:
        return consecutive_count
    return 0


repeat_count = {}
game = Game(1)
hand = game.show_hand(0)
hand.reverse()
includes, freq = game.get_unique_numbers_and_frequencies(0)
includes.reverse()
freq.sort()
freq.reverse()


print(includes, freq)

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
