import os.path
import serial


class Arduino:

    CONST_AMC = [
        '/dev/ttyACM0',
        '/dev/ttyACM1',
        '/dev/ttyACM2',
        '/dev/ttyACM3'
    ]

    def __init__(self) -> None:
        for amc in self.CONST_AMC:
            if os.path.exists(amc):
                self._used_amc = amc
                break

        self._serial = serial.Serial(self._used_amc, 9600)

    def read_serial(self) -> str:
        return self._serial.readline()

    @property
    def amc(self) -> str:
        return self._used_amc


def main() -> None:
    arduino = Arduino()
    print(arduino.read_serial())

if __name__ == '__main__':
    main()
