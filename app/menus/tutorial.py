import pyxel

from ._manager import Menu

from app.components.game.board import Board
from app.components.game.player import Player

from app.ressources.ui.players import tuto
from app.ressources.controls import PlayerControls

class Tutorial(Menu):
    def enter(self):
        self.board = Board(
            Player(
                "tuto",
                tuto,
                PlayerControls()
            ),
            self,
            tile_size=12)

    def draw(self):
        pyxel.cls(4)
        
        self.app.language.Menu.Tutorial.game_description.draw(4,4,1)
        self.board.draw(24,24)

    def update(self):
        self.board.update()
        if pyxel.btnp(pyxel.KEY_T):
            self.app.menu_manager.change_state("main")