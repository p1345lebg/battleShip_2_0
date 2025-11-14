import pyxel

from .menus._manager import MenuManager
from .menus import Main,Tutorial,RessourcePack,Game

from .ressources.controls import PlayerControls
from .ressources.text import english

from .components.game.player import Player


class App:
    def __init__(self):
        pyxel.init(
            width= 256,
            height= 256,
            title="Battle Ship 2.0",
            fps= 60
        )

        pyxel.load("../assets/ressources.pyxres")

        self.language = english.Language

        self.player : list[Player] = [
            Player(
                "player 1",
                0,
                PlayerControls(
                    select = pyxel.KEY_M
                )
            ),
            Player(
                "player 2",
                1,
                PlayerControls(
                    up = pyxel.KEY_Z,
                    down = pyxel.KEY_S,
                    left = pyxel.KEY_LEFT,
                    right = pyxel.KEY_RIGHT,
                    select = pyxel.KEY_V
                )
            )
        ]

        main_menu = Main(self)
        self.menu_manager = MenuManager(
            menus= {
                "main" : main_menu,
                "tutorial" : Tutorial(self),
                "ressourcepack" : RessourcePack(self),
                "game" : Game(self)
            },
            current_state= main_menu
        )

        

    def run(self):
        pyxel.run(self.update, self.draw)

    def update(self):
        self.menu_manager.update()

    def draw(self):
        self.menu_manager.draw()