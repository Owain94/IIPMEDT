from Disk import Disk


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

    @staticmethod
    def get_product_information() -> list:
        li = []

        disk = Disk()
        li.append(disk.get_product_by_index())

        return li

    def add_product(self) -> None:
        """
        Voeg een product toe aan de lijst met producten

        :param product: Het toe te voegen product als string
        """
        self.__user_products.append(self.get_product_information())


def main() -> None:
    user = User()

    print('\n'.join(map(str, user.get_product_information())))

if __name__ == "__main__":
    main()
