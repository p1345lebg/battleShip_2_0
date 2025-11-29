class PlayerUI:
    cursor_color:int
    board_colors : list[int]
    boats_color : int # can not exisist depending on the ressourcepack

    def __init__(
            self,
            cursor_color : int|None = None,
            board_colors : list[int]|None  = None,
            boats_color : int|None = None
        ) -> None:
        self.cursor_color = cursor_color or 0
        self.board_colors = board_colors or [1,2]
        self.boats_color = boats_color or 0


player1ui = PlayerUI(
    6,
    [6,7]
)

player2ui = PlayerUI(
    10,
    [8,9]
)

tuto = PlayerUI(
    1,
    [1,2]
)