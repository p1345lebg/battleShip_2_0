class GridCell:
    def __init__(self, 
            neibourg_up : "GridCell|None", 
            neibourg_down : "GridCell|None",
            neibourg_left : "GridCell|None",
            neibourg_right : "GridCell|None"
        ) -> None:
        self._neibourg_up : GridCell = neibourg_up or self
        self._neibourg_down : GridCell = neibourg_down or self
        self._neibourg_left : GridCell = neibourg_left or self
        self._neibourg_right : GridCell = neibourg_right or self

    @property
    def left(self):
        return self._neibourg_left
    @left.setter
    def left(self, neibourg : "GridCell"):
        self._neibourg_left = neibourg
    
    @property
    def right(self):
        return self._neibourg_right
    @right.setter
    def right(self, neibourg : "GridCell"):
        self._neibourg_right = neibourg
    
    @property
    def up(self):
        return self._neibourg_up
    @up.setter
    def up(self, neibourg : "GridCell"):
        self._neibourg_up = neibourg
    
    @property
    def down(self):
        return self._neibourg_down
    @down.setter
    def down(self, neibourg : "GridCell"):
        self._neibourg_down = neibourg

    def draw(self):
        pass

    def select(self):
        pass