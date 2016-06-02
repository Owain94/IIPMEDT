from Constants import Constants
import RPi.GPIO as GPIO
import time


class Motor:
    def __init__(self, input_pins: list) -> None:
        self.const = Constants(sequence=['1000', '0100', '0010', '0001'])

        GPIO.setmode(GPIO.BCM)

        self.__coil_A_1_pin = input_pins[0]
        self.__coil_A_2_pin = input_pins[1]
        self.__coil_B_1_pin = input_pins[2]
        self.__coil_B_2_pin = input_pins[3]

        GPIO.setup(self.__coil_A_1_pin, GPIO.OUT)
        GPIO.setup(self.__coil_A_2_pin, GPIO.OUT)
        GPIO.setup(self.__coil_B_1_pin, GPIO.OUT)
        GPIO.setup(self.__coil_B_2_pin, GPIO.OUT)

    def set_step(self, step: str) -> bool:
        GPIO.output(self.__coil_A_1_pin, int(step[0]) == 1)
        GPIO.output(self.__coil_A_2_pin, int(step[1]) == 1)
        GPIO.output(self.__coil_B_1_pin, int(step[2]) == 1)
        GPIO.output(self.__coil_B_2_pin, int(step[3]) == 1)

    def up(self, steps: int) -> bool:
        for i in range(steps):
            for step in list(reversed(self.const.sequence)):
                self.set_step(step)
                time.sleep(0.005)
        self.clean()

    def down(self, steps: int) -> bool:
        for i in range(steps):
            for step in self.const.sequence:
                self.set_step(step)
                time.sleep(0.005)
        self.clean()

    def clean(self):
        GPIO.output(self.__coil_A_1_pin, False)
        GPIO.output(self.__coil_A_2_pin, False)
        GPIO.output(self.__coil_B_1_pin, False)
        GPIO.output(self.__coil_B_2_pin, False)


def main() -> None:
    motor = Motor([26, 13, 6, 5])
    motor.up(10)
    motor.down(10)
    GPIO.cleanup()

if __name__ == '__main__':
    main()
