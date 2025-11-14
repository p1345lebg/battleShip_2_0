import pyxel

from ._manager import Menu
from ..components.sprites import Sprite

from ..ressources.images import ui_elements

class Main(Menu):

    def load_sprites(self) -> None:
        self.ui_sprites : dict[str,Sprite] = {
            "space" : Sprite(ui_elements.Keys.space),
            "t" : Sprite(ui_elements.Keys.t)
        }

    def draw(self):
        pyxel.cls(4)

        self.app.language.Menu.Main.start.draw(128-sum(i for i in self.app.language.Menu.Main.start.wlist)/2, pyxel.height/2, 1)
        self.app.language.Menu.Main.tutorial.draw(128-sum(i for i in self.app.language.Menu.Main.tutorial.wlist)/2, pyxel.height/2+ 20, 1)

        

    def update(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.app.menu_manager.change_state("game")
        if pyxel.btnp(pyxel.KEY_T):
            self.app.menu_manager.change_state("tutorial")