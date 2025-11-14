from ...ressources.controls import PlayerControls

class Player:
    def __init__(self, name : str, palette : int, controls : PlayerControls):
        self.__name : str = name
        self.__palette : int = palette
        self.__controls : PlayerControls = controls

    @property
    def name(self):
        return self.__name
    
    @property
    def palette(self):
        return self.__palette
    
    @property
    def controls(self):
        return self.__controls