from time import sleep
from threading import Thread
import RPi.GPIO as GPIO


class Buzzer:
    """
    Klasse om de de buzzer aan te sturen
    """
    def __init__(self, output_pin: int) -> None:
        """
        Code die wordt uitgevoerd bij het instantiëren van de klasse

        :param output_pin: De GPIO pin die wordt gebruikt op de raspberry
                           als int
        """
        self.__buzzer_thread = None
        self.__buzzer_output_pin = output_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.__buzzer_output_pin, GPIO.OUT)

    def buzz(self, seconds: float) -> None:
        """
        Laat de zoomer zoomen door stroom op de GPIO pin te zetten en
        vervolgens de stroom er weer af te halen na een timeout

        :param seconds: secondes als float
        """
        GPIO.output(self.__buzzer_output_pin, True)
        sleep(seconds)
        GPIO.output(self.__buzzer_output_pin, False)
        sleep(seconds)

    def thread_is_alive(self) -> bool:
        """
        Controleert of er een thread bestaat.

        :return: True of False op basis op de thread bestaat, als boolean
        """
        # noinspection PyBroadException
        try:
            return self.__buzzer_thread.is_alive()
        except:
            return False

    def buzz_in_thread(self) -> None:
        """
        Voert de buzz functie uit in een aparte thread zodat er andere
        code tegelijkertijd gedraaid kan worden
        """
        self.__buzzer_thread = Thread(target=self.buzz)
        self.__buzzer_thread.start()


def main() -> None:
    """
    Code om de klasse te testen, deze code wordt niet uitgevoerd als de
    klasse in een ander bestand wordt geimporteerd!
    """
    buzzer = Buzzer(3)  # input pin
    buzzer.buzz(2.0)

# Zorg ervoor dat de main functie niet wordt uitgevoerd als de klasse
# wordt geimporteerd
if __name__ == '__main__':
    main()
