import RPi.GPIO as GPIO
import time
import threading


class Bell:
    def __init__(self, output_pin: int) -> None:
        self.__bell_output_pin = output_pin

    def ring(self, seconds_to_ring: float) -> None:
        GPIO.output(self.__bell_output_pin, True)
        time.sleep(seconds_to_ring)
        GPIO.output(self.__bell_output_pin, False)
        time.sleep(seconds_to_ring)

    def ring_in_thread(self, seconds_to_ring: float) -> None:
        t = threading.Thread(target=self.ring, args=(seconds_to_ring,))
        t.start()


def main() -> None:
    bell = Bell(2)  # input pin
    bell.ring_in_thread(1.0)

if __name__ == '__main__':
    main()
