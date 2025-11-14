from ._text import Text

from app.components.sprites import Sprite
from app.ressources.images.ui_elements import Keys

class Language:
    class Menu:
        class Main:
            start : Text = Text(["press ", Sprite(Keys.space), " to start"])
            tutorial : Text = Text(["press ", Sprite(Keys.t), " for tutorial"])

        class Tutorial:
            game_description : Text = Text(["The goal of this game is to shoot all your\n"
                                            "opponent's boats before he shoot yours"])
            controls : Text = Text(["controls"])
            move : str = "move"
            shoot : str = "shoot"