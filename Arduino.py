from Constants import Constants
from os.path import exists
import serial
import collections


class Arduino:
    """
    Klasse om de serial data van de arduino uit te lezen
    """
    def __init__(self) -> None:
        """
        code die wordt uitgevoerd bij het instantiëren van de klasse
        """

        # De paden op de arduino (gedefinieerd als constante)
        self.const = Constants(amc_paths=[
            '/dev/ttyACM0',
            '/dev/ttyACM1',
            '/dev/ttyACM2',
            '/dev/ttyACM3'
        ])

        # Nakijken welk pad in gebruik is en deze opslaan
        for amc in self.const.amc_paths:
            if exists(amc):
                self.__used_amc = amc
                break

        # Serial instantiëren
        self.__serial = serial.Serial(self.__used_amc, 9600)

    def read_serial(self) -> int:
        """
        Het uitlezen van de data van de arduino

        :return: Gegevens van de POT meter als int, als de uitkomst geen
                 int is zal de functie -1 terug geven
        """
        try:
            return int(self.__serial.readline())
        except:
            return -1

    def get_serial(self) -> int:
        """
        Weg filteren van foutieve data. De arduino geeft soms verkeerde data
        terug. Hier wordt in een lijst met resultaten gekeken welk resultaat
        het vaakst voorkomt. Er kan vanuit worden gegaan dat dit de de juiste
        waarde is

        :return: De waarde die het vaakst voorkomt in de lijst als int
        """
        counter = collections.Counter(self.get_serial_list())

        highest = 0
        d_key = None

        # loop door de hele collectie heem
        for key in counter.keys():
            # Als de waarde die bij de key hoort hoger is dan hetgeen dat we
            # hebben opgeslagen slaan we deze op
            if counter[key] > highest:
                highest = counter[key]
                d_key = key

        # Geeft de meest voorkomende data terug
        return d_key

    def get_serial_list(self) -> list:
        """
        Vraag een lijst op met metingen van de POT meter

        :return: Een lijst met gegevens van de POT meter
        """
        ser_list = []

        for i in range(20):
            while True:
                ser = self.read_serial()
                # Kijk na of de waarde niet hoger is dan 1023 en wel hoger
                # is dan -1, als dit niet het geval is slaan we de data niet
                # op want dan gaat het om foutieve data
                if 1023 >= ser > -1:
                    ser_list.append(ser)
                    break

        return ser_list

    @property
    def amc(self) -> str:
        """
        Getter voor het amc pad dat in gebruik is

        :return: amc pad als string
        """
        return self.__used_amc


def main() -> None:
    """
    Code om de klasse te testen, deze code wordt niet uitgevoerd als de
    klasse in een ander bestand wordt geimporteerd!
    """
    arduino = Arduino()

    for i in range(20):
        print(arduino.get_serial())

# Zorg ervoor dat de main functie niet wordt uitgevoerd als de klasse
# wordt geimporteerd
if __name__ == '__main__':
    main()
