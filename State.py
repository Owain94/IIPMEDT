class State:
    def __init__(self) -> None:
        self._current_state = 'initial'

    def reset_state(self) -> None:
        self._current_state = 'initial'

    def is_state(self, state: str) -> bool:
        return self._current_state is state

    @property
    def current_state(self) -> str:
        return self._current_state

    @current_state.setter
    def current_state(self, value) -> None:
        self._current_state = value
