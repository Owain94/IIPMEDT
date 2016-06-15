from time import sleep
from classes.Arduino import Arduino
from classes.User import User

user = User()
arduino = Arduino()

while True:
    print(user.get_product_information(arduino.read_serial())[0]['name'])
