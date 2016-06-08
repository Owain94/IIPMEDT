import RPi.GPIO as GPIO


class Button:
    """
    Klasse om buttons uit te lezen die verbonden zijn met een raspberry
    """
    def __init__(self, input_pin: int) -> None:
        """
        Code die wordt uitgevoerd bij het instantiëren van de klasse

        :param input_pin: De GPIO pin die wordt gebruikt op de raspberry
                          als int
        """
        self.__button_input_pin = input_pin
        GPIO.setup(self.__button_input_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def is_pressed(self) -> bool:
        """
        Kijk of de button is ingedrukt

        :return: True als de button is ingedrukt, False als deze niet
                 is ingedrukt, als boolean
        """
        # De raspberry geeft false terug als de button is ingedrukt en true
        # als deze niet is ingedrukt, dit is vrij verwarrend vandaar de we
        # return not gebruiken, hiermee draaien we deze logica om
        return not GPIO.input(self.__button_input_pin)


def main() -> None:
    """
    Code om de klasse te testen, deze code wordt niet uitgevoerd als de
    klasse in een ander bestand wordt geimporteerd!
    """
    button = Button(2)
    print(button.is_pressed())

# Zorg ervoor dat de main functie niet wordt uitgevoerd als de klasse
# wordt geimporteerd
if __name__ == '__main__':
    main()
