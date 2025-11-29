import pyxel

from ._manager import Menu
from ..components.sprites import Sprite # pyright: ignore[reportUnusedImport]

from ..ressources.ui import ui_elements # pyright: ignore[reportUnusedImport]

class Main(Menu):
    def draw(self):
        pyxel.cls(4)

        self.app.language.Menu.Main.start.draw(128-self.app.language.Menu.Main.start.w/2, pyxel.height/2, 1)
        self.app.language.Menu.Main.tutorial.draw(128-sum(i for i in self.app.language.Menu.Main.tutorial.wlist)/2, pyxel.height/2+ 20, 1)

    def update(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.app.menu_manager.change_state("game")
        if pyxel.btnp(pyxel.KEY_T):
            self.app.menu_manager.change_state("tutorial")