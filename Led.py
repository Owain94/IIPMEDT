import RPi.GPIO as GPIO
import time


class Led:
    def __init__(self, output_pin: int) -> None:
        self.__led_output_pin = output_pin

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.__led_output_pin, GPIO.OUT)

    def blink(self, seconds: float):
        GPIO.output(self.__led_output_pin, GPIO.HIGH)
        time.sleep(seconds)
        GPIO.output(self.__led_output_pin, GPIO.LOW)
        time.sleep(seconds)


def main() -> None:
    led = Led(12)  # input pin
    led.blink(2)

if __name__ == '__main__':
    main()
