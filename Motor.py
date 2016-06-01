import RPi.GPIO as GPIO


class Motor:

    def __init__(self, input_pins: list):
        GPIO.setup(input_pins[0], GPIO.OUT)
        GPIO.setup(input_pins[1], GPIO.OUT)
        GPIO.setup(input_pins[2], GPIO.OUT)
        GPIO.setup(input_pins[3], GPIO.OUT)


def main() -> None:
    Motor([17, 18, 27, 22])

if __name__ == '__main__':
    main()
