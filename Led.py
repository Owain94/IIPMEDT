import RPi.GPIO as GPIO
import time
import threading


class Led:
    def __init__(self, output_pin: int) -> None:
        self.__blink_thread = None
        self.__led_output_pin = output_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.__led_output_pin, GPIO.OUT)

    def blink(self, seconds: float):
        GPIO.output(self.__led_output_pin, True)
        time.sleep(seconds)
        GPIO.output(self.__led_output_pin, False)
        time.sleep(seconds)

    def thread_is_alive(self) -> bool:
        try:
            return self.__blink_thread.is_alive()
        except:
            return False

    def blink_in_thread(self, seconds: float):
        self.__blink_thread = threading.Thread(target=self.blink, args=(seconds,))
        self.__blink_thread.start()


def main() -> None:
    led = Led(2)  # input pin
    led.blink_in_thread(4.0)
    time.sleep(5.0)
    print(led.thread_is_alive())
    time.sleep(10.0)
    print(led.thread_is_alive())

if __name__ == '__main__':
    main()
