from time import sleep
from threading import Thread
import RPi.GPIO as GPIO


class Buzzer:
    """
    Klasse om de de bel aan te sturen
    """
    def __init__(self, output_pin: int) -> None:
        """
        Code die wordt uitgevoerd bij het instantiëren van de klasse

        :param output_pin: De GPIO pin die wordt gebruikt op de raspberry
                           als int
        """
        self.__buzz_thread = None
        self.__buzz_output_pin = output_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.__buzz_output_pin, GPIO.OUT)

    def buzz(self, seconds_to_ring: float) -> None:
        """
        Laat de zoomer zoomen door stroom op de GPIO pin te zetten en
        vervolgens de stroom er weer af te halen na een timeout

        :param seconds_to_ring: De tijd die tussen het rinkelen van de
                                bel zit als float
        """
        GPIO.output(self.__buzz_output_pin, True)
        sleep(seconds_to_ring)
        GPIO.output(self.__buzz_output_pin, False)
        sleep(seconds_to_ring)

    def thread_is_alive(self) -> bool:
        # noinspection PyBroadException
        try:
            return self.__buzz_thread.is_alive()
        except:
            return False

    def buzz_in_thread(self, seconds_to_ring: float) -> None:
        """
        Voer de buzz functie uit in een aparte thread zodat er andere
        code tegelijkertijd gedraaid kan worden

        :param seconds_to_ring: De tijd die tussen het rinkelen van de
                                bel zit als float
        """
        self.__buzz_thread = Thread(target=self.buzz, args=(seconds_to_ring,))
        self.__buzz_thread.start()


def main() -> None:
    """
    Code om de klasse te testen, deze code wordt niet uitgevoerd als de
    klasse in een ander bestand wordt geimporteerd!
    """
    bell = Buzzer(2)  # input pin
    bell.buzz_in_thread(1.0)

# Zorg ervoor dat de main functie niet wordt uitgevoerd als de klasse
# wordt geimporteerd
if __name__ == '__main__':
    main()