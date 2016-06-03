from Constants import Constants
import os.path
import serial
import collections


class Arduino:
    def __init__(self) -> None:
        self.const = Constants(amc_paths=[
            '/dev/ttyACM0',
            '/dev/ttyACM1',
            '/dev/ttyACM2',
            '/dev/ttyACM3'
        ])

        for amc in self.const.amc_paths:
            if os.path.exists(amc):
                self.__used_amc = amc
                break

        self.__serial = serial.Serial(self.__used_amc, 9600)

    def read_serial(self) -> int:
        try:
            return int(self.__serial.readline())
        except:
            return -1

    def get_serial(self) -> int:
        counter = collections.Counter(self.get_serial_list())

        highest = 0
        d_key = None

        for key in counter.keys():
            if counter[key] > highest:
                highest = counter[key]
                d_key = key

        return d_key

    def get_serial_list(self) -> list:
        ser_list = []

        for i in range(20):
            while True:
                ser = self.read_serial()
                if 1023 >= ser > -1:
                    ser_list.append(ser)
                    break

        return ser_list

    @property
    def amc(self) -> str:
        return self.__used_amc


def main() -> None:
    arduino = Arduino()

    for i in range(20):
        print(arduino.get_serial())

if __name__ == '__main__':
    main()
