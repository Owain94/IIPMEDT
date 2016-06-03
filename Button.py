import RPi.GPIO as GPIO


class Button:
    def __init__(self, input_pin: int) -> None:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(input_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        self.__button = GPIO.input(input_pin)

    def is_pressed(self) -> bool:
        return self.__button == False


def main() -> None:
    button = Button(2)
    print(button.is_pressed())

if __name__ == '__main__':
    main()
