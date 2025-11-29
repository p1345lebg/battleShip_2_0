import pyxel

class Menu:
    START : int = pyxel.KEY_SPACE

class PlayerControls:
    up : int = pyxel.KEY_UP
    down : int = pyxel.KEY_DOWN
    left : int = pyxel.KEY_LEFT
    right : int = pyxel.KEY_RIGHT
    select : int = pyxel.KEY_SPACE

    def __init__(self,
            up : int|None = None,
            down : int|None = None,
            left : int|None = None,
            right : int|None = None,
            select : int|None = None
    ) -> None:
        if up:
            self.up = up
        if down:
            self.down = down
        if left:
            self.left = left
        if right:
            self.right = right
        if select:
            self.select = select