import pyxel

#from app import App

from ._manager import Menu
from app.components.game.board import Board
from app.components.game.player import Player

from app.ressources.text._text import Text


class StatWindow:
    def  __init__(self, player : Player) -> None:
        self.player : Player = player

    def draw(self, x : float, y : float):
        coins = Text(["coins : ",self.player.coin_str])
        player_name = Text([self.player.name])
        pyxel.rectb(
            x+4,
            y+4,
            120,
            120,
            self.player.palette.cursor_color
        )
        player_name.draw(x+8,y+8+pyxel.FONT_HEIGHT,1)
        coins.draw(x+8,y+16+pyxel.FONT_HEIGHT,1)


class Game(Menu):
    def enter(self):
        self.boards : dict[tuple[float,float],Board] = {
            (0,0) : Board(self.app.player[0], self),
            (128,128) : Board(self.app.player[1], self)
        }
        self.stat_windows : dict[tuple[int,int], StatWindow] = {
            (0,128) : StatWindow(self.app.player[0]),
            (128,0) : StatWindow(self.app.player[1])
        }

    def draw(self):
        pyxel.cls(4)
        for (x,y),board in self.boards.items():
            board.draw(x,y)

        for (x,y),window in self.stat_windows.items():
            window.draw(x,y)

    def update(self):
        for board in self.boards.values():
            board.update()

        if pyxel.btnp(pyxel.KEY_SPACE):
            self.app.menu_manager.change_state("main")

