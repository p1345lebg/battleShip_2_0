from ._text import Text

from app.components.sprites import Sprite
from app.ressources.ui.ui_elements import Keys

class Language:
    class Menu:
        class Main:
            title : Text = Text(["battleship"])
            start : Text = Text(["press ", Sprite(Keys.space), " to start"])
            tutorial : Text = Text(["press ", Sprite(Keys.t), " for tutorial"])

        class Tutorial:
            game_description : Text = Text(["The goal of this game is to shoot all your\n"
                                            "opponent's boats before he shoot yours"])
            controls : Text = Text(["controls"])
            move : Text = Text(["move"])
            shoot : Text = Text(["shoot"])