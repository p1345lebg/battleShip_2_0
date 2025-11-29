from pyxel import Image

class SpriteParameters:
    img : Image|int = 0
    u : float = 0
    v : float = 0
    w : float = 8
    h : float = 8
    colkey : int|None = None
    rotate : float|None = None
    scale : float|None = None

    def __init__(
            self,
            img : Image|int,
            u : float,
            v : float,
            w : float,
            h : float,
            colkey : int|None = None,
            /,
            rotate : float|None = None,
            scale : float|None = None
            ) -> None:
        self.img = img
        self.u = u
        self.v = v
        self.w = w
        self.h = h
        self.colkey = colkey
        self.rotate = rotate
        self.scale = scale

        self.__dict__ = {
            "img" : self.img,
            "u" : self.u,
            "v" : self.v,
            "w" : self.w,
            "h" : self.h,
            "colkey" : self.colkey,
            "rotate" : self.rotate,
            "scale" : self.scale
        }

    def __eq__(self, value: object) -> bool:
        return (
            (
                self.img == value.img and
                self.u == value.u and
                self.v == value.v and
                self.w == value.w and
                self.h == value.h and 
                self.colkey == value.colkey
            ) if type(value) == SpriteParameters else False
        )


class SpriteAnimatedParemeters(SpriteParameters):
    frames_between : int = 10
    sprites : list[SpriteParameters] = [

    ]
    loop : bool = False
    static_at_end : bool = False

    def __init__(
            self,
            frames_between : int,
            sprites : list[SpriteParameters],
            loop : bool = False,
            static_at_end : bool = False
            ) -> None:
        self.frames_between : int = frames_between
        self.sprites : list[SpriteParameters] = sprites
        self.loop : bool = loop
        self.static_at_end : bool = static_at_end
        self.curent_sprite : int = 0

        self.__dict__ = {
            "u" : self.sprites[self.curent_sprite].u,
            "v" : self.sprites[self.curent_sprite].v,
            "w" : self.sprites[self.curent_sprite].w,
            "h" : self.sprites[self.curent_sprite].h,
            "colkey" : self.sprites[self.curent_sprite].colkey,
            "self.rotate" : self.sprites[self.curent_sprite].rotate,
            "scale" : self.sprites[self.curent_sprite].scale
        }

    def __eq__(self, value: object) -> bool:
        return (
            (
                self.frames_between == value.frames_between and
                self.sprites == value.sprites and 
                self.loop == value.loop and
                self.static_at_end == value.static_at_end
            ) if type(value) == SpriteAnimatedParemeters else False
        )



def change_images(ressourcepack_name : str):
    pass