class User:
    """
    Klasse om bij te houden welke producten de gebruiker allemaal
    heeft toegevoegd
    """
    def __init__(self):
        """
        Code die wordt uitgevoerd bij het instantiëren van de klasse
        """
        self.__user_products = []

    def add_product(self, product: str) -> None:
        """
        Voeg een product toe aan de lijst met producten

        :param product: Het toe te voegen product als string
        """
        self.__user_products.append(product)
