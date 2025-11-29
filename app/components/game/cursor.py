import pyxel

if __name__ == "__main__":
    from .board import Board

from .player import Player

class Cursor:
    def __init__(self, board : "Board", player : Player, x : int = 0, y : int = 0) -> None:
        self.board : "Board" = board
        self.player = player
        self.__x : int = x if 0 <= x < self.board.width else 0
        self.__y : int = y if 0 <= x < self.board.height else 0

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, new : int):
        if 0 <= new < self.board.width:
            self.__x = new

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, new : int):
        if 0 <= new < self.board.width:
            self.__y = new

    
    def draw(self, board_x : float, board_y : float):
        pyxel.rectb(
            board_x+self.x*self.board.tile_size,
            board_y+self.y*self.board.tile_size,
            self.board.tile_size,
            self.board.tile_size,
            self.player.palette.cursor_color
        )
        pyxel.rectb(
            board_x+self.x*self.board.tile_size-1,
            board_y+self.y*self.board.tile_size-1,
            self.board.tile_size+2,
            self.board.tile_size+2,
            self.player.palette.cursor_color
        )
    
    def update(self):
        if pyxel.btnp(self.player.controls.up):
            self.y -= 1
        if pyxel.btnp(self.player.controls.down):
            self.y += 1
        if pyxel.btnp(self.player.controls.left):
            self.x -= 1
        if pyxel.btnp(self.player.controls.right):
            self.x += 1
        