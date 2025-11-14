import pyxel

from ...ressources.images._parameters import SpriteParameters

class Sprite:
    def __init__(self, parameters : SpriteParameters) -> None:
        self.parameters : SpriteParameters = parameters

    def draw(self, x : float,y : float):
        pyxel.blt(
            x = x,
            y = y,
            img = self.parameters.img,
            u = self.parameters.u,
            v = self.parameters.v,
            w = self.parameters.w,
            h = self.parameters.h,
            colkey = self.parameters.colkey,
            rotate = self.parameters.rotate,
            scale = self.parameters.scale
        )

    @property
    def w(self) -> float:
        return self.parameters.w

    @property
    def h(self) -> float:
        return self.parameters.h