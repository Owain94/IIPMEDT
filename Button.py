import RPi.GPIO as GPIO


class Button:
    def __init__(self, input_pin: int) -> None:
        self.__button_input_pin = input_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.__button_input_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def is_pressed(self) -> bool:
        return not GPIO.input(self.__button_input_pin)


def main() -> None:
    button = Button(2)
    print(button.is_pressed())

if __name__ == '__main__':
    main()
