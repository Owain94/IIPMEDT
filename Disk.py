from xml.dom import minidom
from Arduino import Arduino
from Constants import Constants


class Disk:
    """
    Klasse om xml bestanden te verwerken
    """

    def __init__(self) -> None:
        """
        Code die wordt uitgevoerd bij het instantiëren van de klasse
        """
        self.const = Constants(max_index=1024)
        # Inladen van het xml bestand met de producten
        document = minidom.parse('xml/products.xml')
        # Alle producten inlezen
        self._products = document.getElementsByTagName("product")
        # De range voor de prodcuten bereken op basis van de maximale
        # index en het aantal producten
        self._disk_range = round(self.const.max_index / len(self._products),
                                 2)
        # Het aantal producten
        self._product_count = len(self._products)
        # Arduino
        self._arduino = Arduino()

    def get_serial(self) -> int:
        """
        Leest de waarde uit van de POT meter.

        :return: POT waarde als int
        """
        return self._arduino.get_serial()

    def get_product_index(self, potential: int) -> int:
        """
        Product index ophalen aan de hand van de POT meet gegevens

        :param potential: POT meet gegevens als int
        :return: product index als int
        """
        for i in range(0, self._product_count):
            if (potential >= i * self._disk_range)\
                    and (potential <= ((i + 1) * self._disk_range)):
                return i

    def get_by_key(self, key: str, potential: int) -> str:
        """
        De opgegeven key(name, score, kcal, sugar of fat) wordt uitgelezen
        van het huidig geselecteerde product. Deze waarde wordt terug gegeven.

        :param potential: POT meet gegevens als int
        :param key: name, score, kcal, sugar of fat als string
        :return: Aantal kcal als string
        """
        index = self.get_product_index(potential)
        return self._products[index].getElementsByTagName(key)[0] \
            .firstChild.data

    def get_product_by_index(self, potential: int = -1) -> list:
        """
        Haalt een list van een product op aan de hand van de POT meet
        gegevens

        :param potential: POT meet gegevens als int
        :return: Aantal kcal als string
        """
        potential = self.potential(potential)

        return {
            'name': self.get_product_name_by_index(potential),
            'score': self.get_product_score_by_index(potential),
            'kcal': self.get_product_kcal_by_index(potential),
            'sugar': self.get_product_sugar_by_index(potential),
            'fat': self.get_product_fat_by_index(potential)
        }

    def get_product_name_by_index(self, potential: int = -1) -> str:
        """
        Haal de naam van een product op aan de hand van de POT meet
        gegevens

        :param potential: POT meet gegevens als int
        :return: Aantal kcal als string
        """
        return self.get_by_key('name', self.potential(potential))

    def get_product_score_by_index(self, potential: int = -1) -> str:
        """
        Haal de score van een product op aan de hand van de POT meet
        gegevens

        :param potential: POT meet gegevens als int
        :return: Product score als string
        """
        return self.get_by_key('score', self.potential(potential))

    def get_product_kcal_by_index(self, potential: int = -1) -> str:
        """
        Haal het aantal kcal van een product op aan de hand van de POT
        meet gegevens

        :param potential: POT meet gegevens als int
        :return: Aantal kcal als string
        """
        return self.get_by_key('kcal', self.potential(potential))

    def get_product_sugar_by_index(self, potential: int = -1) -> str:
        """
        Haal het suiker percentage van een product op aan de hand van de
        POT meet gegevens

        :param potential: POT meet gegevens als int
        :return: Suiker percentage als string
        """
        return self.get_by_key('sugar', self.potential(potential))

    def get_product_fat_by_index(self, potential: int = -1) -> str:
        """
        Haal het vet percentage van een product op aan de hand van de
        POT meet gegevens

        :param potential: POT meet gegevens als int
        :return: Vet percentage als string
        """
        return self.get_by_key('fat', self.potential(potential))

    def potential(self, potential: int) -> int:
        """
        Kijkt of de opgegeven potential niet gelijk is aan -1 (standaard).
        Als dat zo is wordt de potmeter uitgelezen. Als de gebruik een eigen
        waarde opgegeven heeft wordt de potmeter niet opnieuw uitgelezen maar
        wordt die waarde gebruikt.

        :param potential: POT meet gegevens als int
        :return: POT meet gegevens als int (zelf ingevoerd of uitgelezen)
        """
        if potential is -1:
            potential = self.get_serial()

        return potential

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

    @property
    def arduino(self) -> Arduino:
        """
        Getter voor de Arduino instantie

        :return: Een Arduino object
        """
        return self._arduino


def main() -> None:
    """
    Code om de klasse te testen, deze code wordt niet uitgevoerd als de
    klasse in een ander bestand wordt geimporteerd!
    """
    disk = Disk()
    print(disk.get_product_name_by_index(250))
    print(disk.get_product_score_by_index(250))
    print(disk.get_product_kcal_by_index(250))
    print(disk.get_product_sugar_by_index(250))
    print(disk.get_product_fat_by_index(250))
    print(disk.get_product_by_index(250))


# Zorg ervoor dat de main functie niet wordt uitgevoerd als de klasse
# wordt geimporteerd
if __name__ == '__main__':
    main()
