from time import sleep
from threading import Thread
import RPi.GPIO as GPIO


class Led:
    """
    Klasse om LED lampjes aan te sturen
    """
    def __init__(self, output_pin: int) -> None:
        """
        Code die wordt uitgevoerd bij het instantiëren van de klasse

        :param output_pin: De GPIO pin die wordt gebruikt op de raspberry
                           als int
        """
        self.__blink_thread = None
        self.__led_output_pin = output_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.__led_output_pin, GPIO.OUT)

    def blink(self, seconds: float) -> None:
        """
        Laat een LED knipperen door stroom op de GPIO pin te zetten en
        vervolgens de stroom er weer af te halen na een timeout

        :param seconds: De tijd die tussen het knipperen van de LED zit
                        als float
        """
        GPIO.output(self.__led_output_pin, True)
        sleep(seconds)
        GPIO.output(self.__led_output_pin, False)
        sleep(seconds)

    def thread_is_alive(self) -> bool:
        """
        Controleert of er een thread bestaat.

        :return: True of False op basis op de thread bestaat, als boolean
        """
        # noinspection PyBroadException
        try:
            return self.__blink_thread.is_alive()
        except:
            return False

    def blink_in_thread(self, seconds: float):
        """
        Voer de blink functie uit in een aparte thread zodat er andere
        code tegelijkertijd gedraaid kan worden

        :param seconds: De tijd die tussen het knipperen van de LED zit
                        als float
        """
        self.__blink_thread = Thread(target=self.blink, args=(seconds,))
        self.__blink_thread.start()


def main() -> None:
    """
    Code om de klasse te testen, deze code wordt niet uitgevoerd als de
    klasse in een ander bestand wordt geimporteerd!
    """
    led = Led(2)  # input pin
    led.blink_in_thread(4.0)
    sleep(5.0)
    print(led.thread_is_alive())
    sleep(10.0)
    print(led.thread_is_alive())

# Zorg ervoor dat de main functie niet wordt uitgevoerd als de klasse
# wordt geimporteerd
if __name__ == '__main__':
    main()
