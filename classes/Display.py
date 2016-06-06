import math
import time

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

        self.const = Constants(digits=[
            {
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
            }
        ])

    def comma(self) -> None:
        """
        Zet de komma op het display.

        :return: HELEMAAL NIETS!
        """
        self.__display.set_pixel(3, 7, 1)

    # def zero(self, first_digit: bool) -> None:

    def digit(self, digit: int, second: bool) -> None:


def main() -> None:
    """
    Code om de klasse te testen, deze code wordt niet uitgevoerd als de
    klasse in een ander bestand wordt geimporteerd!
    """
    display = Display()
    display.digit(2, True)

# Zorg ervoor dat de main functie niet wordt uitgevoerd als de klasse
# wordt geimporteerd
if __name__ == '__main__':
    main()
