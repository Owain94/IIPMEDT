from time import sleep
import RPi.GPIO as GPIO

pins = [1, 2, 3, 4, 5]

GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

for pin in pins:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    for pin in pins:
        print("pin: {}, pressed: {}".format(pin, GPIO.input(pin)))

    sleep(1)
    print('\n\n')