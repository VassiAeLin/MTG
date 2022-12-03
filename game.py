import player
from deck import Deck
import random
from consts import MESSAGES

class Game:

    def __init__(self) -> None:
        self.bot = None
        self.player = None
        self.deck = Deck()
    @staticmethod
    def _start(message):
        while True:
            answer = input(message)
            if answer == "n":
                return False
            elif answer == "y":
                return True

    def _launching(self):
        color_p = input("Выберите цвет колоды: ").lower()
        if color_p == "черный":
            color_b = "белый"
        elif color_p == "белый":
            color_b = "черный"
            # # первая рука
            # for i in range(8):
            #     print(self.deck.get_cards_w())

        self.bot = player.Bot(position = False, color = color_b)
        for i in range(8):
            self.bot.new_card()
        print(self.bot, 'is create')
        
        
        self.player = player.Player(position = True, color=color_p)
        for i in range(8):
            self.player.new_card()

    def put_mana(self):
        if self.player.position == True:
            self.player.change_mana()
        else: self.bot.change_mana()

    def start_game(self):
        message = MESSAGES.get('_start')
        if not self._start(message = message):
            exit(1)

        self._launching()
        self.player.list()

        # self.put_mana()