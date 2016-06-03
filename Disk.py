from xml.dom import minidom


class Disk:
    """
    Klasse om xml bestanden te verwerken
    """
    def __init__(self, max_index: int) -> None:
        """
        Code die wordt uitgevoerd bij het instantiëren van de klasse

        :param max_index: Maximale index die kan worden terug gegeven door
                          de POT meter als int
        """
        self._max = max_index
        # Inladen van het xml bestand met de producten
        document = minidom.parse('xml/products.xml')

        # Alle producten inlezen
        self._products = document.getElementsByTagName("product")
        # De range voor de prodcuten bereken op basis van de maximale
        # index en het aantal producten
        self._disk_range = round(self._max / len(self._products), 2)
        # Het aantal producten
        self._product_count = len(self._products)

    def get_product_index(self, potential: int) -> int:
        """
        Product index ophalen aan de hand van de POT meet gegevens

        :param potential: POT meet gegevens als int
        :return: product index als int
        """
        for i in range(0, self._product_count):
            if (potential >= i * self._disk_range) and (
                        potential <= ((i + 1) * self._disk_range)):
                return i

    def get_by_key(self, key: str, potential: int) -> str:
        """
        TODO

        :param potential: POT meet gegevens als int
        :param key: TODO als string
        :return: Aantal kcal als string
        """
        index = self.get_product_index(potential)
        return self._products[index].getElementsByTagName(key)[0]\
            .firstChild.data

    def get_product_name_by_index(self, potential: int) -> str:
        """
        Haal de naam van een product op aan de hand van de POT meet
        gegevens

        :param potential: POT meet gegevens als int
        :return: Aantal kcal als string
        """
        return self.get_by_key('name', potential)

    def get_product_score_by_index(self, potential: int) -> str:
        """
        Haal de score van een product op aan de hand van de POT meet
        gegevens

        :param potential: POT meet gegevens als int
        :return: Product score als string
        """
        return self.get_by_key('score', potential)

    def get_product_kcal_by_index(self, potential: int) -> str:
        """
        Haal het aantal kcal van een product op aan de hand van de POT
        meet gegevens

        :param potential: POT meet gegevens als int
        :return: Aantal kcal als string
        """
        return self.get_by_key('kcal', potential)

    def get_product_sugar_by_index(self, potential: int) -> str:
        """
        Haal het suiker percentage van een product op aan de hand van de
        POT meet gegevens

        :param potential: POT meet gegevens als int
        :return: Suiker percentage als string
        """
        return self.get_by_key('sugar', potential)

    def get_product_fat_by_index(self, potential: int) -> str:
        """
        Haal het vet percentage van een product op aan de hand van de
        POT meet gegevens

        :param potential: POT meet gegevens als int
        :return: Vet percentage als string
        """
        return self.get_by_key('fat', potential)

    @property
    def products(self) -> list:
        """
        Getter voor alle prodcuten

        :return: Alle producten als lijst
        """
        return self._products

    @property
    def disk_range(self) -> float:
        """
        Getter voor de disk range

        :return: Disk range als int
        """
        return self._disk_range

    @property
    def product_count(self) -> int:
        """
        Getter voor het aantal producten

        :return: Het aantal producten als int
        """
        return self._product_count


def main() -> None:
    """
    Code om de klasse te testen, deze code wordt niet uitgevoerd als de
    klasse in een ander bestand wordt geimporteerd!
    """
    disk = Disk(1024)
    print(disk.get_product_name_by_index(250))
    print(disk.get_product_score_by_index(250))
    print(disk.get_product_kcal_by_index(250))
    print(disk.get_product_sugar_by_index(250))
    print(disk.get_product_fat_by_index(250))

# Zorg ervoor dat de main functie niet wordt uitgevoerd als de klasse
# wordt geimporteerd
if __name__ == '__main__':
    main()
