class State:
    """
    Klasse om bij te houden waar het programma zich bevindt in de flow
    """

    def __init__(self) -> None:
        """
        Code die wordt uitgevoerd bij het instantiëren van de klasse
        """
        self.__current_state = 'initial'
        self.__step = 0
        self.__count = 0

    def reset_state(self) -> None:
        """
        Herstel de huidige staat van het programma naar de begin waarde
        """
        self.__current_state = 'initial'

    def reset_step(self) -> None:
        """
        Herstel de huidige stap van het programma naar de begin waarde
        """
        self.__step = 0

    def reset_count(self) -> None:
        """
        Herstelt de huidige count naar de begin waarde.
        """
        self.__count = 0

    def is_state(self, state: str) -> bool:
        """
        Kijk of de huidige staat van het programma gelijk is aan meegegeven
        argument

        :param state: Staat om na te kijken als string
        :return: True als de huidige staat dezelfde is als de staat om na
        te kijken anders False, als boolean
        """
        return self.__current_state is state

    def is_count(self, count: int = 100) -> bool:
        """
        Controleert of het opgegeven getal gelijk is aan de count.
        :param count: getal om te controleren

        :return: True of False
        """
        return self.__count is count

    def count_up(self) -> None:
        """
        Telt de count met 1 op.
        """
        self.__count += 1

    def status(self) -> None:
        """
        Print de huidige status voor debuggen
        """
        #print('Stap: ' + str(self.step))
        #print('Huidige status: ' + self.current_state)
        #print('Count:' + str(self.count))
        pass

    @property
    def current_state(self) -> str:
        """
        Getter voor de huidige staat

        :return: De huidige staat als string
        """
        return self.__current_state

    @current_state.setter
    def current_state(self, value) -> None:
        """
        Setter om de huidige state van het programma aan te passen

        :param value: De nieuwe staat als string
        """
        self.__current_state = value

    @property
    def count(self) -> int:
        """
        Getter voor de huidige count

        :return: De huidige count als int
        """
        return self.__count

    @property
    def step(self) -> int:
        """
        Getter voor de huidige stap

        :return: De huidige stap als int
        """
        return self.__step

    @step.setter
    def step(self, value) -> None:
        """
        Setter om de huidige stap van het programma mee aan te passen

        :param value: De huidige stap als int
        """
        self.__step = value
