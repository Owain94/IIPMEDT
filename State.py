class State:
    def __init__(self) -> None:
        self.current_state = 'initial'

    def reset_state(self) -> None:
        self.current_state = 'initial'

    def is_state(self, state: str) -> bool:
        return self.current_state is state

    @property
    def current_state(self) -> str:
        return self.current_state

    @current_state.setter
    def current_state(self, current_state) -> None:
        self.current_state = current_state
