from Disk import Disk
from time import sleep

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

    def add_product(self) -> None:
        """
        Voeg een product toe aan de lijst met producten

        :param product: Het toe te voegen product als string
        """
        self.__user_products.append(self.get_product_information())

    def calculate_score(self) -> float:
        """
        Reken totale score uit van de gekozen producten
        """
        score = 0
        count = 0 
        kcal = 0 
        for product_list in self.__user_products:
            for product in product_list:
                score += product['score']
                kcal += product['kcal']
                count += 1 
       	
       	kcal_score = kcal / 80
        score = (score / count) / 2

        final_score = (0.7 * kcal_score) + (0.3 * score)

        return final_score

    @staticmethod
    def get_product_information() -> list:
        """
        Haalt de live waarde van POT meter op en haalt het daarbij horende
        product op.

        :return: list met alle producten
        """
        li = []

        disk = Disk()
        li.append(disk.get_product_by_index())

        return li

    @property
    def user_products(self) -> list:
        """
        Lijst met alle producten van de gebruiker.

        :return: list met producten
        """
        return self.__user_products


def main() -> None:
    user = User()

    for i in range(10):
        user.add_product()

    user.calculate_score()

if __name__ == "__main__":
    main()
