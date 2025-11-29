from .grid_cell import GridCell 

class Grid:
    def __init__(self, current_cell : GridCell, *cells : GridCell) -> None:
        self.current_cell : GridCell = current_cell
        self.cells : list[GridCell] = list(cells)
        
    def move_right(self):
        self.current_cell = self.current_cell.right

    def move_left(self):
        self.current_cell = self.current_cell.left

    def move_up(self):
        self.current_cell = self.current_cell.up

    def move_down(self):
        self.current_cell = self.current_cell.down