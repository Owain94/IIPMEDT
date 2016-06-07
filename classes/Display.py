if __name__ == '__main__':
    from sys import path
    path.append("..")

from util.Constants import Constants
from lib.Matrix8x8 import Matrix8x8
from time import sleep


#  I2C SETUP
#  https://learn.adafruit.com/matrix-7-segment-led-backpack-with-the-raspberry-pi/configuring-your-pi-for-i2c
#  https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c
class Display:
    """
    Klasse om displays aan te sturen
    """
    def __init__(self, display_address: int) -> None:
        """
        Code die wordt uitgevoerd bij het instantiëren van de klasse
        :param display_address: str
        """
        self.__display_address = display_address
        self.__display = Matrix8x8(address=self.__display_address, busnum=1)
        self.__display.begin()
        self.__display.clear()

        self.const = Constants(digits={
            1: [
                [2, 2],
                [2, 3],
                [2, 4],
                [2, 5],
                [2, 6]
            ],

            2: [
                [0, 2],
                [1, 2],
                [2, 2],
                [2, 3],
                [2, 4],
                [1, 4],
                [0, 4],
                [0, 5],
                [0, 6],
                [1, 6],
                [2, 6],
            ],

            3: [
                [2, 2],
                [2, 3],
                [2, 4],
                [2, 5],
                [2, 6],
                [0, 2],
                [1, 2],
                [1, 4],
                [0, 4],
                [1, 6],
                [0, 6]
            ],

            4: [
                [0, 2],
                [0, 3],
                [0, 4],
                [1, 4],
                [2, 4],
                [2, 2],
                [2, 3],
                [2, 4],
                [2, 5],
                [2, 6]
            ],

            5: [
                [0, 6],
                [1, 6],
                [2, 6],
                [2, 5],
                [2, 4],
                [1, 4],
                [0, 4],
                [0, 3],
                [0, 2],
                [1, 2],
                [2, 2]
            ],

            6: [
                [2, 2],
                [1, 2],
                [0, 2],
                [0, 3],
                [0, 4],
                [0, 5],
                [0, 6],
                [1, 6],
                [2, 6],
                [2, 5],
                [2, 4],
                [1, 4]
            ],

            7: [
                [0, 2],
                [1, 2],
                [2, 2],
                [2, 2],
                [2, 3],
                [2, 4],
                [2, 5],
                [2, 6]
            ],

            8: [
                [2, 2],
                [2, 3],
                [2, 4],
                [2, 5],
                [2, 6],
                [0, 2],
                [0, 3],
                [0, 4],
                [0, 5],
                [0, 6],
                [1, 2],
                [1, 4],
                [1, 6]
            ],

            9: [
                [2, 2],
                [2, 3],
                [2, 4],
                [2, 5],
                [2, 6],
                [0, 2],
                [0, 3],
                [0, 4],
                [0, 6],
                [1, 2],
                [1, 4],
                [1, 6]
            ],

            0: [
                [2, 2],
                [2, 3],
                [2, 4],
                [2, 5],
                [2, 6],
                [0, 2],
                [0, 3],
                [0, 4],
                [0, 5],
                [0, 6],
                [1, 2],
                [1, 6]
            ]
        })

    def comma(self) -> None:
        """
        Zet de komma op het display.
        """
        self.__display.set_pixel(3, 7, 1)
        self.__display.write_display()

    def digit(self, digit: int, second: bool = False) -> None:
        """
        Zet het opgeven getal op het display.

        :param digit: 0 t/m 9
        :param second: of het opgegeven getal het eerste of tweede getal is
        """
        pixels = self.const.digits[digit]

        # for pixel in pixels:
        #    x = int([pixel[0] + 5, pixel[0]][not second])
        #    y = int(pixel[1])
        #    self.__display.set_pixel(x, y, 1)

        [(self.__display.set_pixel(int([pixel[0] + 5,
                                        pixel[0]][not second]),
                                   int(pixel[1]), 1))
         for pixel in pixels]

        self.__display.write_display()

    def clear(self) -> None:
        """
        Zet alle pixels van het display weer uit.
        """
        # for x in range(8):
        #    for y in range(8):
        #        self.__display.clear()
        #        self.__display.set_pixel(x, y, 0)
        #        self.__display.write_display()

        [(self.__display.clear(),
          self.__display.set_pixel(x, y, 0),
          self.__display.write_display())
         for x in range(8) for y in range(8)]

    def show_digit(self, score: float) -> None:
        """
        Converteer float naar de display digits

        :param score: Score als float
        """
        self.clear()

        digit = "{:1.1f}".format(score)
        self.digit(int(digit[0]))
        self.comma()
        self.digit(int(digit[2]), True)

    @property
    def display_number(self) -> int:
        """
        Haal het display nummer op.
        :return: display nummer als int.
        """
        if self.__display_address is 0x70:
            return 1
        elif self.__display_address is 0x71:
            return 2


def main() -> None:
    """
    Code om de klasse te testen, deze code wordt niet uitgevoerd als de
    klasse in een ander bestand wordt geimporteerd!
    """
    display_one = Display(0x70)
    display_one.show_digit(1.0)
    display_two = Display(0x71)
    display_two.show_digit(2.0)

    sleep(10)
    display_one.clear()
    display_two.clear()

# Zorg ervoor dat de main functie niet wordt uitgevoerd als de klasse
# wordt geimporteerd
if __name__ == '__main__':
    main()
