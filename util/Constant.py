class Constant(object):
    """
    Klasse om constante variabele aan te kunnen maken
    """

    def __init__(self, *args, **kwargs) -> None:
        """
        Code die wordt uitgevoerd bij het instantiëren van de klasse

        :param args: args
        :param kwargs: kwargs
        """
        self._d = dict(*args, **kwargs)

    def __iter__(self) -> iter:
        """
        Implementeer iteraties voor de dictionary met attributen

        :return: iteratie van de dictionary als iter
        """
        return iter(self._d)

    def __len__(self) -> int:
        """
        Geeft het aantal attributen terug

        :return: het aantal attributen als int
        """
        return len(self._d)

    def __getattr__(self, name: str) -> any:
        """
        Getter voor een attribuut

        :param name: Attribuut naam als string
        :return: Attribuut waarde als *
        """
        return self._d[name]

    def __setattr__(self, name: str, value: any) -> None:
        """
        Attribuut setter

        :param name: Attribuut naam als string
        :param value: Attribuut value als *
        """
        if name[0] == '_':
            super(Constants, self).__setattr__(name, value)
        else:
            raise ValueError("setattr while locked", self)
