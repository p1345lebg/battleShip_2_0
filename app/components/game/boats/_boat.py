from app.ressources.images._parameters import SpriteParameters,SpriteAnimatedParemeters

class Boat:
    relative_positions : list[tuple[int,int]]

    textures : dict[tuple[int,int], SpriteParameters|SpriteAnimatedParemeters] = {}