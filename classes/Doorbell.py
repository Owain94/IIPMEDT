from time import sleep
from threading import Thread
import RPi.GPIO as GPIO


class Doorbell:
    """
    Klasse om de de bel aan te sturen
    """
    def __init__(self, audio_track_length: float, output_pin: int) -> None:
        """
        Code die wordt uitgevoerd bij het instantiëren van de klasse

        :param audio_track_length: De lengte van het audio bestand
        :param output_pin: De GPIO pin die wordt gebruikt op de raspberry
                           als int
        """
        self.__doorbell_thread = None
        self.__doorbell_output_pin = output_pin
        self.__doorbell_audio_track_length = audio_track_length
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.__doorbell_output_pin, GPIO.OUT)

    def bell(self) -> None:
        """
        Laat de bel bellen door stroom op de GPIO pin te zetten en
        vervolgens de stroom er weer af te halen na een timeout
        """
        GPIO.output(self.__doorbell_output_pin, True)
        sleep(self.__doorbell_audio_track_length)
        GPIO.output(self.__doorbell_output_pin, False)
        sleep(1.0)

    def thread_is_alive(self) -> bool:
        """
        Controleert of er een thread bestaat.

        :return: True of False op basis op de thread bestaat, als boolean
        """
        # noinspection PyBroadException
        try:
            return self.__doorbell_thread.is_alive()
        except:
            return False

    def bell_in_thread(self) -> None:
        """
        Voert de bel functie uit in een aparte thread zodat er andere
        code tegelijkertijd gedraaid kan worden
        """
        self.__doorbell_thread = Thread(target=self.bell)
        self.__doorbell_thread.start()


def main() -> None:
    """
    Code om de klasse te testen, deze code wordt niet uitgevoerd als de
    klasse in een ander bestand wordt geimporteerd!
    """
    doorbell = Doorbell(2.0, 3)  # input pin
    doorbell.bell()

# Zorg ervoor dat de main functie niet wordt uitgevoerd als de klasse
# wordt geimporteerd
if __name__ == '__main__':
    main()
