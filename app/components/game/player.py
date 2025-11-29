from ...ressources.controls import PlayerControls

from app.ressources.ui.players import PlayerUI

class Player:
    def __init__(self, name : str, palette : PlayerUI, controls : PlayerControls, coins : int|None = None):
        self.__name : str = name
        self.__palette : PlayerUI = palette
        self.__controls : PlayerControls = controls
        self.__coins : int = coins or 0
        self.coin_str : str = str(self.coins)

    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def palette(self) -> PlayerUI:
        return self.__palette
    
    @property
    def controls(self) -> PlayerControls:
        return self.__controls
    
    @property
    def coins(self):
        return self.__coins
    
    @coins.setter
    def coins(self, n : int):
        self.__coins = n
        self.coin_str : str = str(self.coins)
