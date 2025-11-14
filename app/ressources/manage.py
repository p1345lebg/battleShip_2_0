import pyxel

from .images._parameters import change_images
from .sounds import change_sounds


def change_ressources(ressourcepack_name : str, image : bool = False, sounds : bool = False):
    pyxel.load(
        f"assets/{ressourcepack_name}/ressources.pyxres", 
        exclude_images= not image,
        exclude_tilemaps= not image,
        exclude_sounds= not sounds,
        exclude_musics= not sounds
    )
    change_images(ressourcepack_name)
    change_sounds(ressourcepack_name)

custom_images : list[pyxel.Image] = []