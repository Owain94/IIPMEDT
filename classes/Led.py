from time import sleep
from threading import Thread, ThreadError
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
        GPIO.setup(self.__led_output_pin, GPIO.OUT)

    def blink(self, seconds: float, sleep_after_blink: bool = True) -> None:
        """
        Laat een LED knipperen door stroom op de GPIO pin te zetten en
        vervolgens de stroom er weer af te halen na een timeout

        :param sleep_after_blink: Of er gewacht moet worden na het aanzetten
                        van de led als bool
        :param seconds: De tijd die tussen het knipperen van de LED zit
                        als float
        """
        GPIO.output(self.__led_output_pin, True)
        sleep(seconds)
        GPIO.output(self.__led_output_pin, False)
        if sleep_after_blink:
            sleep(seconds)

    def thread_is_alive(self) -> bool:
        """
        Controleert of er een thread bestaat.

        :return: True of False op basis op de thread bestaat, als boolean
        """
        # noinspection PyBroadException
        try:
            return self.__blink_thread.is_alive()
        except ThreadError as e:
            errno, strerror = e.args
            print("Exception ({0}): {1}".format(errno, strerror))
            return False

    def blink_in_thread(self, seconds: float, sleep_after_blink: bool = True):
        """
        Voer de blink functie uit in een aparte thread zodat er andere
        code tegelijkertijd gedraaid kan worden

        :param sleep_after_blink: Of er gewacht moet worden na het aanzetten
                        van de led als bool
        :param seconds: De tijd die tussen het knipperen van de LED zit
                        als float
        """
        self.__blink_thread = Thread(target=self.blink,
                                     args=(seconds, sleep_after_blink))
        self.__blink_thread.start()


def main() -> None:
    """
    Code om de klasse te testen, deze code wordt niet uitgevoerd als de
    klasse in een ander bestand wordt geimporteerd!
    """
    led_start = Led(12)  # input pin
    led_start.blink_in_thread(1.0)

    led_red_plus = Led(20)
    led_green_plus = Led(16)

    led_red_plus.blink_in_thread(1.0)
    sleep(3)
    led_green_plus.blink_in_thread(1.0)


# Zorg ervoor dat de main functie niet wordt uitgevoerd als de klasse
# wordt geimporteerd
if __name__ == '__main__':
    main()
