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
        if os.path.exists("/dev/ttyACM0") == True:
            self._used_amc = '/dev/ttyACM0'
        if os.path.exists("/dev/ttyACM1") == True:
            self._used_amc = '/dev/ttyACM1'
        if os.path.exists("/dev/ttyACM2") == True:
            self._used_amc = '/dev/ttyACM2'
        if os.path.exists("/dev/ttyACM3") == True:
            self._used_amc = '/dev/ttyACM3'


    def read_serial(self) -> str:
        ser = serial.Serial(self._used_amc, 9600)
        return ser.readline()

    @property
    def amc(self) -> str:
        return self._used_amc


def main() -> None:
    arduino = Arduino()
    print(int(arduino.read_serial()))

if __name__ == '__main__':
    main()
