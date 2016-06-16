if __name__ == '__main__':
    from sys import path

    path.append("..")

from xml.dom import minidom
from classes.Arduino import Arduino
from util.Constants import Constants
from util.Helpers import prefix


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
        document = minidom.parse(prefix() + 'datafiles/products.xml')
        # document = minidom.parse('../datafiles/products.xml')
        # Alle producten inlezen
        self.__products = document.getElementsByTagName("product")
        # De range voor de prodcuten bereken op basis van de maximale
        # index en het aantal producten
        self.__disk_range = (self.const.max_index /
                              len(self.__products))
        # Het aantal producten
        self.__product_count = len(self.__products)
        # Arduino
        self.__arduino = Arduino()

    def get_serial(self) -> int:
        """
        Leest de waarde uit van de POT meter.

        :return: POT waarde als int
        """
        return self.__arduino.get_serial()

    def get_product_index(self, potential: int) -> int:
        """
        Product index ophalen aan de hand van de POT meet gegevens

        :param potential: POT meet gegevens als int
        :return: product index als int
        """
        for i in range(0, self.__product_count):
            if (potential >= i * self.__disk_range) \
                    and (potential <= ((i + 1) * self.__disk_range)):
                return i

    @staticmethod
    def get_product_index_v2(potential_number: float) -> int:

        potential_number = int(potential_number)

        # if 0 >= potential_number >= 36:
        if potential_number >= 0 and potential_number <= 36:
            return 0

        # elif 37 >= potential_number >= 66:
        elif potential_number >= 37 and potential_number <= 66:
            return 1

        # elif 67 >= potential_number >= 93:
        elif potential_number >= 67 and potential_number <= 93:
            return 2

        # elif 94 >= potential_number >= 118:
        elif potential_number >= 94 and potential_number <= 118:
            return 3

        # elif 119 >= potential_number >= 147:
        elif potential_number >= 119 and potential_number <= 147:
            return 4

        # elif 148 >= potential_number >= 174:
        elif potential_number >= 148 and potential_number <= 174:
            return 5

        # elif 175 >= potential_number >= 202:
        elif potential_number >= 175 and potential_number <= 202:
            return 6

        # elif 203 >= potential_number >= 233:
        elif potential_number >= 203 and potential_number <= 233:
            return 7

        # elif 234 >= potential_number >= 264:
        elif potential_number >= 234 and potential_number <= 264:
            return 8

        # elif 265 >= potential_number >= 297:
        elif potential_number >= 265 and potential_number <= 297:
            return 9

        # elif 298 >= potential_number >= 329:
        elif potential_number >= 298 and potential_number <= 329:
            return 10

        # elif 330 >= potential_number >= 362:
        elif potential_number >= 330 and potential_number <= 362:
            return 11

        # elif 363 >= potential_number >= 397:
        elif potential_number >= 363 and potential_number <= 397:
            return 12

        # elif 398 >= potential_number >= 429:
        elif potential_number >= 398 and potential_number <= 429:
            return 13

        # elif 430 >= potential_number >= 463:
        elif potential_number >= 430 and potential_number <= 463:
            return 14

        # elif 464 >= potential_number >= 497:
        elif potential_number >= 464 and potential_number <= 497:
            return 15

        # elif 498 >= potential_number >= 529:
        elif potential_number >= 498 and potential_number <= 529:
            return 16

        # elif 530 >= potential_number >= 564:
        elif potential_number >= 530 and potential_number <= 564:
            return 17

        # elif 565 >= potential_number >= 594:
        elif potential_number >= 565 and potential_number <= 594:
            return 18

        # elif 595 >= potential_number >= 626:
        elif potential_number >= 595 and potential_number <= 626:
            return 19

        # elif 627 >= potential_number >= 658:
        elif potential_number >= 627 and potential_number <= 658:
            return 20

        # elif 659 >= potential_number >= 687:
        elif potential_number >= 659 and potential_number <= 687:
            return 21

        # elif 688 >= potential_number >= 718:
        elif potential_number >= 688 and potential_number <= 718:
            return 22

        # elif 719 >= potential_number >= 747:
        elif potential_number >= 719 and potential_number <= 747:
            return 23

        # elif 748 >= potential_number >= 778:
        elif potential_number >= 748 and potential_number <= 778:
            return 24

        # elif 779 >= potential_number >= 808:
        elif potential_number >= 779 and potential_number <= 808:
            return 25

        # elif 809 >= potential_number >= 836:
        elif potential_number >= 809 and potential_number <= 836:
            return 26

        # elif 837 >= potential_number >= 866:
        elif potential_number >= 837 and potential_number <= 866:
            return 27

        # elif 867 >= potential_number >= 893:
        elif potential_number >= 867 and potential_number <= 893:
            return 28

        # elif 894 >= potential_number >= 928:
        elif potential_number >= 894 and potential_number <= 928:
            return 29

        # elif 929 >= potential_number >= 959:
        elif potential_number >= 929 and potential_number <= 959:
            return 30

        # elif 960 >= potential_number >= 988:
        elif potential_number >= 960 and potential_number <= 988:
            return 31

        # elif 989 >= potential_number >= 1018:
        elif potential_number >= 989 and potential_number <= 1018:
            return 32

        elif potential_number >= 1019:
            return 33

    def get_by_key(self, key: str, potential: int) -> str:
        """
        De opgegeven key(name, score, kcal, sugar of fat) wordt uitgelezen
        van het huidig geselecteerde product. Deze waarde wordt terug gegeven.

        :param potential: POT meet gegevens als int
        :param key: name, score, kcal, sugar of fat als string
        :return: Aantal kcal als string
        """
        index = self.get_product_index_v2(potential)
        return self.__products[index].getElementsByTagName(key)[0] \
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
        :return: POT meet gegevens (zelf ingevoerd of uitgelezen), als int
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
        return self.__products

    @property
    def disk_range(self) -> float:
        """
        Getter voor de disk range

        :return: Disk range als int
        """
        return self.__disk_range

    @property
    def product_count(self) -> int:
        """
        Getter voor het aantal producten

        :return: Het aantal producten als int
        """
        return self.__product_count

    @property
    def arduino(self) -> Arduino:
        """
        Getter voor de Arduino instantie

        :return: Instantie van de Arduino klasse
        """
        return self.__arduino


def main() -> None:
    """
    Code om de klasse te testen, deze code wordt niet uitgevoerd als de
    klasse in een ander bestand wordt geimporteerd!
    """
    disk = Disk()
    while True:
        print("Productnaam:" + disk.get_product_name_by_index())
        # print("Index:" + str(disk.get_product_index_v2(disk.get_serial())))
        # print("Potential:" + str(disk.get_serial()))


# Zorg ervoor dat de main functie niet wordt uitgevoerd als de klasse
# wordt geimporteerd
if __name__ == '__main__':
    main()
