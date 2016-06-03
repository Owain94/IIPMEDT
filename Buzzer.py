from time import sleep
from threading import Thread
import RPi.GPIO as GPIO


class Buzzer:
    """
    Klasse om de de bel aan te sturen
    """
    def __init__(self, output_pin: int) -> None:
        """
        code die wordt uitgevoerd bij het instantiëren van de klasse

        :param output_pin: De GPIO pin die wordt gebruikt op de raspberry
        """
        self.__bell_output_pin = output_pin

    def ring(self, seconds_to_ring: float) -> None:
        """
        Laat de bel rinkelen door stroom op de GPIO pin te zetten en
        vervolgens de stroom er weer af te halen na een timeout

        :param seconds_to_ring: De tijd die tussen het rinkelen van de
                                bel zit
        """
        GPIO.output(self.__bell_output_pin, True)
        sleep(seconds_to_ring)
        GPIO.output(self.__bell_output_pin, False)
        sleep(seconds_to_ring)

    def ring_in_thread(self, seconds_to_ring: float) -> None:
        """
        Voer de ring functie uit in een aparte thread zodat er andere
        code tegelijkertijd gedraaid kan worden

        :param seconds_to_ring: De tijd die tussen het rinkelen van de
                                bel zit
        """
        t = Thread(target=self.ring, args=(seconds_to_ring,))
        t.start()


def main() -> None:
    """
    Code om de klasse te testen, deze code wordt niet uitgevoerd als de
    klasse in een ander bestand wordt geimporteerd!
    """
    bell = Bell(2)  # input pin
    bell.ring_in_thread(1.0)

# Zorg ervoor dat de main functie niet wordt uitgevoerd als de klasse
# wordt geimporteerd
if __name__ == '__main__':
    main()
