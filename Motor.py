import RPi.GPIO as GPIO
import time


class Motor:

    CONST_SEQUENCE = ['1000', '0100', '0010', '0001']

    def __init__(self, input_pins: list) -> None:

        GPIO.setmode(GPIO.BCM)

        self._coil_A_1_pin = input_pins[0]
        self._coil_A_2_pin = input_pins[1]
        self._coil_B_1_pin = input_pins[2]
        self._coil_B_2_pin = input_pins[3]

        GPIO.setup(self._coil_A_1_pin, GPIO.OUT)
        GPIO.setup(self._coil_A_2_pin, GPIO.OUT)
        GPIO.setup(self._coil_B_1_pin, GPIO.OUT)
        GPIO.setup(self._coil_B_2_pin, GPIO.OUT)

    def set_step(self, step: str) -> bool:
        GPIO.output(self._coil_A_1_pin, int(step[0]) == 1)
        GPIO.output(self._coil_A_2_pin, int(step[1]) == 1)
        GPIO.output(self._coil_B_1_pin, int(step[2]) == 1)
        GPIO.output(self._coil_B_2_pin, int(step[3]) == 1)

    def up(self, steps: int) -> bool:
        for i in range(steps):
            for step in list(reversed(self.CONST_SEQUENCE)):
                self.set_step(step)
                time.sleep(0.005)
        GPIO.cleanup()

    def down(self, steps: int) -> bool:
        for i in range(steps):
            for step in self.CONST_SEQUENCE:
                self.set_step(step)
                time.sleep(0.005)
        GPIO.cleanup()


def main() -> None:
    motor = Motor([26, 13, 6, 5])
    motor.up(1)
    motor.down(1)

if __name__ == '__main__':
    main()
