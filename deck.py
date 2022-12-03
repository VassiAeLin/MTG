from consts import type_w, property_w, type_m, property_mb, property_mw
from consts import type_b, property_b, manacount
from itertools import product
import random
from random import shuffle


class Card():
    def __init__(self, type, property, mana):
        self.type = type
        self.property = property
        self.mana = mana
        self.turn = False
        # photo = ''

class Creature(Card):
    def __init__(self, type, property, mana):
        super().__init__(type, property, mana)
        self.pw = random.randint(self.mana-1, self.mana+1)
        self.xp = random.randint(self.mana-1, self.mana+1)
        self.turn = False

class Magic(Card):
    def __init__(self, type, property, mana):
        super().__init__(type, property, mana)

class Mana():
    turn = True

class Deck:
    def __init__(self):
        self.cards_w = self._createdeck_w()
        shuffle(self.cards_w)
        self.cards_b = self._createdeck_b()
        shuffle(self.cards_b)

    def _createmb(self):
        for type, property, mana in product(type_m, property_mb, manacount):
            c = Magic(type=type, property=property, mana=mana)

    def _createdeck_w(self):
        cards = []
        ccards = []
        mcards = []
        for type, property, mana in product(type_w, property_w, manacount):
            c = Creature(type=type, property=property, mana=mana)
            ccards.append(c)
        for type, property, mana in product(type_m, property_mw, manacount):
            c = Magic(type=type, property=property, mana=mana)
            mcards.append(c)
        for i in range(20):
            c = Mana()
            cards.append(c)
            cards.append(random.choice(ccards))
            cards.append(random.choice(mcards))
        return cards

    def _createdeck_b(self):
            cards = []
            ccards = []
            mcards = []
            for type, property, mana in product(type_b, property_b, manacount):
                c = Creature(type=type, property=property, mana=mana)
                ccards.append(c)
            for type, property, mana in product(type_m, property_mb, manacount):
                c = Magic(type=type, property=property, mana=mana)
                mcards.append(c)
            for i in range(20):
                c = Mana()
                cards.append(c)
                cards.append(random.choice(ccards))
                cards.append(random.choice(mcards))
            return cards

    def get_cards_w(self):
        return self.cards_w.pop()

    def get_cards_b(self):
        return self.cards_b.pop()

# class Field():
#     def __init__(self):
#         self.field = []
#         self.graevary = []