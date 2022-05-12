import collections
# randomise choose card
from random import choice

# Creating named tuple from collection
Card = collections.namedtuple('Card', ['rank', 'suit'])


# Creating Class for modeling card deck

class cardDeck(object):
    # init rank of card
    # x = [expression], converting into list
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        # init deck using namedtuple
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        # get length of all deck
        return len(self._cards)

    def __getitem__(self, position):
        # get item at his position
        return self._cards[position]


# Sorted card deck with high values as spades
# dictionary with higher -> lower values
suit_values = dict(spades = 3, hearts = 2, diamonds = 1, clubs = 0)

def spades_high(card):
    # getting ranks for card
    rank_value = cardDeck.ranks.index(card.rank)
    # 0 = '2' clubs && 21 = 'A' spades
    return rank_value * len(suit_values) + suit_values[card.suit]

if __name__ == "__main__":

    print('# ---------------------------------------------- #')
    beer_card = Card('7', 'diamonds')
    print(beer_card, type(beer_card))

    print('# --------------------------------------------- #')
    deck = cardDeck()
    print(len(deck))
    print(deck[-1])

    print('# -------------Choice----------------------------#')
    for _ in range(5):
        print(choice(deck))

    print('# --------------doctest------------------------- #')
    for card in deck: # doctest: +ELLIPSIS
        print(card)

    print('#---------------Sorted-with-key-------------------#')
    for card in sorted(deck, key=spades_high): # doctest: -ELLIPSIS
        print(card)
