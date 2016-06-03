from Constants import Constants
import RPi.GPIO as GPIO
from time import sleep


class Motor:
    """
    Klasse om een motor aan te sturen
    """
    def __init__(self, input_pins: list) -> None:
        """
        code die wordt uitgevoerd bij het instantiëren van de klasse

        :param input_pins: De GPIO pins waar de motor op is aan gesloten
        """
        # De sequentie die wordt gebruikt om de motor te laten draaien
        # (gedefinieerd als constante)
        self.const = Constants(sequence=['1000', '0100', '0010', '0001'])

        GPIO.setmode(GPIO.BCM)

        self.__coil_A_1_pin = input_pins[0]
        self.__coil_A_2_pin = input_pins[1]
        self.__coil_B_1_pin = input_pins[2]
        self.__coil_B_2_pin = input_pins[3]

        GPIO.setup(self.__coil_A_1_pin, GPIO.OUT)
        GPIO.setup(self.__coil_A_2_pin, GPIO.OUT)
        GPIO.setup(self.__coil_B_1_pin, GPIO.OUT)
        GPIO.setup(self.__coil_B_2_pin, GPIO.OUT)

    def set_step(self, step: str) -> None:
        """
        TODO

        :param step: Het aantal stappen als string
        """
        GPIO.output(self.__coil_A_1_pin, int(step[0]) == 1)
        GPIO.output(self.__coil_A_2_pin, int(step[1]) == 1)
        GPIO.output(self.__coil_B_1_pin, int(step[2]) == 1)
        GPIO.output(self.__coil_B_2_pin, int(step[3]) == 1)

    def up(self, steps: int) -> None:
        """
        Laat de motor vooruit draaien

        :param steps: Het aantal stappen dat er gedraaid moet worden als int
        """
        for i in range(steps):
            # Lees de sequntie achterstevoren in
            for step in list(reversed(self.const.sequence)):
                self.set_step(step)
                sleep(0.005)
        self.clean()

    def down(self, steps: int) -> None:
        """
        Laat de motor achteruit draaien

        :param steps: Het aantal stappen dat er gedraaid moet worden als int
        """
        for i in range(steps):
            for step in self.const.sequence:
                self.set_step(step)
                sleep(0.005)
        self.clean()

    def clean(self) -> None:
        """
        Haal de stroom van alle GPIO pinnen die worden gebruikt
        """
        GPIO.output(self.__coil_A_1_pin, False)
        GPIO.output(self.__coil_A_2_pin, False)
        GPIO.output(self.__coil_B_1_pin, False)
        GPIO.output(self.__coil_B_2_pin, False)


def main() -> None:
    """
    Code om de klasse te testen, deze code wordt niet uitgevoerd als de
    klasse in een ander bestand wordt geimporteerd!
    """
    motor = Motor([26, 13, 6, 5])
    motor.up(10)
    motor.down(10)
    GPIO.cleanup()

# Zorg ervoor dat de main functie niet wordt uitgevoerd als de klasse
# wordt geimporteerd
if __name__ == '__main__':
    main()
