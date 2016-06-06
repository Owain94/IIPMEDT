if __name__ == '__main__':
    from sys import path
    path.append("..")

from util.Constants import Constants
from lib.Matrix8x8 import Matrix8x8


class Display:
    """
    Klasse om displays aan te sturen
    """
    def __init__(self) -> None:
        """
        Code die wordt uitgevoerd bij het instantiëren van de klasse
        """
        self.__display = Matrix8x8()
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

    def digit(self, digit: int, second: bool = False) -> None:
        """
        Zet het opgeven getal op het display.

        :param digit: 0 t/m 9
        :param second: of het opgegeven getal het eerste of tweede getal is
        """
        pixels = self.const.digits[digit]

        for pixel in pixels:
            x = int([pixel[0] + 5, pixel[0]][not second])
            y = int(pixel[1])
            self.__display.set_pixel(x, y, 1)

        self.__display.write_display()

    def clear(self) -> None:
        for x in range(8):
            for y in range(8):
                self.__display.clear()
                self.__display.set_pixel(x, y, 0)
                self.__display.write_display()


def main() -> None:
    """
    Code om de klasse te testen, deze code wordt niet uitgevoerd als de
    klasse in een ander bestand wordt geimporteerd!
    """
    display = Display()
    display.clear()
    display.digit(6)
    display.comma()
    display.digit(9, True)

# Zorg ervoor dat de main functie niet wordt uitgevoerd als de klasse
# wordt geimporteerd
if __name__ == '__main__':
    main()
