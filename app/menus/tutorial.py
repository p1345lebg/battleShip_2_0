import pyxel

from ._manager import Menu

class Tutorial(Menu):
    def draw(self):
        pyxel.cls(4)
        
        self.app.language.Menu.Tutorial.game_description.draw(4,4,1)

    def update(self):
        if pyxel.btnp(pyxel.KEY_T):
            self.app.menu_manager.change_state("main")