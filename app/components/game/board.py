import pyxel

from .cursor import Cursor
from .player import Player

if __name__ == "__main__":
    from app.menus._manager import Menu

class Board:
    def __init__(self, player : Player, menu : "Menu", tile_size : int = 16) -> None:
        self.menu = menu
        self.player : Player = player
        self.width : int = 8
        self.height : int = 8
        self.tile_size : int = tile_size
        self.tiles_dict : dict[tuple[int,int],str] = {}
        self.cursors : list[Cursor] = []
        for p in self.menu.app.player:
            if p != self.player:
                self.cursors.append(Cursor(self, p))

    def select(self, x : int, y : int) -> bool:
        if self.tiles_dict[(x,y)] : # a completer
            return True
        return False
    
    def update(self):
        for cursor in self.cursors:
            cursor.update()
    
    def draw(self, x : float, y : float):
        for j in range(self.width):
            for i in range(self.height):
                pyxel.rect(
                    x+i*self.tile_size,
                    y+j*self.tile_size,
                    self.tile_size,
                    self.tile_size,
                    self.player.palette.board_colors[(i+j)%len(self.player.palette.board_colors)]
                )
        for cursor in self.cursors:
            cursor.draw(x,y)