from .sprite import Sprite
from .sprite_container import SpriteContainer

class SpriteAnimated(SpriteContainer, Sprite):
    def __init__(self, 
                frames_between : int,
                *sprites : Sprite,
                loop : bool = False,
                static_at_end : bool = False
            ):
        super().__init__(*sprites)
        self.frames_between : int = frames_between
        self.current_frame = 0
        self.max_frame : int = len(self.sprites)

    @property
    def w(self) -> float:
        return self.sprites[self.current_frame].w

    @property
    def h(self) -> float:
        return self.sprites[self.current_frame].h