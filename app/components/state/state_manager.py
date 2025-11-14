from .state import State

class StateManager:
    def __init__(self, states_dict : dict[str, State], current_state : State) -> None:
        self.states : dict[str, State] = states_dict
        self.current_state : State = current_state

    def add_states(self, state_dict : dict[str, State]):
        for key, value in state_dict.items():
            self.states[key] = value

    def remove_state(self, state_name : str):
        if state_name in self.states.keys():
            self.states.pop(state_name)

    def get_available_states(self) -> list[str]:
        return list(self.states.keys())

    def change_state(self, state_name : str) -> None:
        if not state_name in self.get_available_states():
            print(f"state {state_name} does not exist")
            return
        
        self.current_state.exit()
        self.current_state = self.states[state_name]
        self.current_state.enter()

    def update(self):
        self.current_state.update()