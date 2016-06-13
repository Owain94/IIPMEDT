from time import sleep
from threading import Thread, ThreadError
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
        self.__ringtone_thread = None
        self.__buzzer_output_pin = output_pin
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

    def ringtone(self, tones: list) -> None:
        """
        Een methode die een leuk deuntje afspeelt.
        :param tones: lijst met tonen die afgespeeld moeten worden.
        """
        for tone in tones:
            self.buzz(tone)

    def buzz_in_thread(self, seconds: float) -> None:
        """
        Voert de buzz functie uit in een aparte thread zodat er andere
        code tegelijkertijd gedraaid kan worden

        :param seconds:
        """
        self.__buzzer_thread = Thread(target=self.buzz, args=(seconds,))
        self.__buzzer_thread.start()

    def ringtone_in_thread(self, tones: list) -> None:
        """
        Voert de ringtone functie uit in een aparte thread zodat er andere
        code tegelijkertijd gedraaid kan worden

        :param tones: lijst met tonen als list
        """
        self.__ringtone_thread = Thread(target=self.ringtone, args=(tones,))
        self.__ringtone_thread.start()

    @staticmethod
    def thread_is_alive(thread: Thread) -> bool:
        """
        Controleert of de opgegeven thread bestaat.

        :param thread: Thread
        :return: True of False op basis op de thread bestaat, als boolean
        """
        # noinspection PyBroadException
        try:
            return thread.is_alive()
        except ThreadError as e:
            print("Exception (Buzzer, thread_is_alive: {0})".format(e))
            return False
        except AttributeError as e:
            print("Exception (Buzzer, thread_is_alive: {0})".format(e))
            return False

    def buzzer_is_alive(self) -> bool:
        """
        Controleert of de buzzer thread bestaat

        :return: True of False op basis op de thread bestaat, als boolean
        """
        return self.thread_is_alive(self.__buzzer_thread)

    def ringtone_is_alive(self) -> bool:
        """
        Controleert of de ringtone thread bestaat

        :return: True of False op basis op de thread bestaat, als boolean
        """
        return self.thread_is_alive(self.__ringtone_thread)


def main() -> None:
    """
    Code om de klasse te testen, deze code wordt niet uitgevoerd als de
    klasse in een ander bestand wordt geimporteerd!
    """
    buzzer = Buzzer(25)  # input pin
    buzzer.ringtone_in_thread([0.8])
    sleep(1)
    print(buzzer.ringtone_is_alive())
    GPIO.cleanup()


# Zorg ervoor dat de main functie niet wordt uitgevoerd als de klasse
# wordt geimporteerd
if __name__ == '__main__':
    main()
