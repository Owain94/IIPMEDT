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
            ACM = '/dev/ttyACM0'
        if os.path.exists("/dev/ttyACM1") == True:
            ACM = '/dev/ttyACM1'
        if os.path.exists("/dev/ttyACM2") == True:
            ACM = '/dev/ttyACM2'
        if os.path.exists("/dev/ttyACM3") == True:
            ACM = '/dev/ttyACM3'

        ser = serial.Serial(ACM, 9600)
        read_serial = ser.readline()

        try:
            print(read_serial)

        except:
            pass


def main() -> None:
    arduino = Arduino()

if __name__ == '__main__':
    main()
