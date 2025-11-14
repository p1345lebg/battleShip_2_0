if __name__ == "__main__":
    from .. import App # pyright: ignore[reportUnusedImport]

from ..components.state.state_manager import StateManager
from ..components.state.state import State

from ..components.sprites import Sprite

class Menu(State):
    def __init__(self, app) -> None: # type: ignore
        super().__init__()
        self.app : "App" = app
        self.sprites : dict[str, Sprite]
        self.load_sprites()

    def load_sprites(self):
        pass

    def draw(self):
        pass


class MenuManager(StateManager) :
    def __init__(self, menus: dict[str, Menu], current_state: Menu) -> None:
        self.states : dict[str, Menu] = menus # type: ignore
        self.current_state : Menu = current_state # type: ignore

    def draw(self):
        self.current_state.draw()