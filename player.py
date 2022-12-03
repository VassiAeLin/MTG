import abc
import deck
from deck import Deck

class NonPlayer(abc.ABC):
    def __init__(self, position: bool, color: str):
        self.cards = []
        self.health = 20
        self.position = position
        self.color = color
        self.mana = 0

    def new_card(self):
        if self.color == "черный":
            card = Deck.get_cards_b
        else:
            card = Deck.get_cards_w
        self.cards.append(card)
        return print(card)

    # def change_mana(self):
    #     pass

class Player(NonPlayer):
    pass
    # def change_mana(self):
    #     for i in self.cards:
    #         if i == deck.Mana():
    #             value = input("Хотите положить ману?(y/n) ")
    #             if value == 'y': 
    #                 self.mana +=1
    #                 self.cards.pop(i)
    #                 for j in self.cards:
    #                     print(self.cards[j])
    #                     break
    #             if value == 'n':
    #                 break


class Bot(NonPlayer):
    pass
    # def change_mana(self):
    #     for i in self.cards:
    #         if i == deck.Mana():
    #             self.mana +=1
    #             break