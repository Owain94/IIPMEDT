import os.path
import serial


class Arduino:
    def __init__(self) -> None:
        self.amc_paths = [
            '/dev/ttyACM0',
            '/dev/ttyACM1',
            '/dev/ttyACM2',
            '/dev/ttyACM3'
        ]

        for amc in self.amc_paths:
            if os.path.exists(amc):
                self.__used_amc = amc
                break

        self.__serial = serial.Serial(self.__used_amc, 9600)

    def read_serial(self) -> str:
        return self.__serial.readline()

    @property
    def amc(self) -> str:
        return self.__used_amc


def main() -> None:
    arduino = Arduino()
    print(arduino.read_serial())

if __name__ == '__main__':
    main()
