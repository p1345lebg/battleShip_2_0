import pyxel

from ._manager import Menu

class Game(Menu):
    def draw(self):
        pyxel.cls(1)

    def update(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.app.menu_manager.change_state("main")