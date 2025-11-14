from .sprite import Sprite

class SpriteContainer:
    def __init__(self, *sprites : Sprite):
        self.sprites : list[Sprite] = list(sprites)

    def add_sprites(self, *sprites : Sprite):
        self.sprites += list(sprites)

    def kill_sprite(self, sprite : Sprite):
        self.sprites.remove(sprite)