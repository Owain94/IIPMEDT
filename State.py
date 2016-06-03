class State:
    """
    Klasse om bij te houden waar het programma zich bevindt in de flow
    """
    def __init__(self) -> None:
        """
        Code die wordt uitgevoerd bij het instantiëren van de klasse
        """
        self._current_state = 'initial'

    def reset_state(self) -> None:
        """
        Herstel de huidige staat van het programma naar de begin waarde
        """
        self._current_state = 'initial'

    def is_state(self, state: str) -> bool:
        """
        Kijk of de huidige staat van het programma gelijk is aan meegegeven
        argument

        :param state: Staat om na te kijken als string
        :return: True als de huidige staat dezelfde is als de stata om na
        te kijken anders False, als boolean
        """
        return self._current_state is state

    @property
    def current_state(self) -> str:
        """
        Getter voor de huidige staat

        :return: De huidige staat als string
        """
        return self._current_state

    @current_state.setter
    def current_state(self, value) -> None:
        """
        Setter om de huidige stata van het programma aan te passen

        :param value: De nieuwe staat als string
        """
        self._current_state = value
