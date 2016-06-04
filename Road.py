from Button import Button
from Motor import Motor


class Road:

    def __init__(self,
                 begin_switch_input_pin: int,
                 end_switch_input_pin: int,
                 motor_input_pins: list
                 ):

        self.__begin_switch = Button(begin_switch_input_pin)
        self.__end_switch = Button(end_switch_input_pin)
        self.__motor = Motor(motor_input_pins)

    def move_to_begin(self) -> bool:
        while not self.__begin_switch.is_pressed():
            self.__motor.down(1)

        self.__motor.up(20)

        return True

    def move_to_end(self) -> bool:
        while not self.__end_switch.is_pressed():
            self.__motor.up(1)

        self.motor.down(20)

        return True

    @property
    def begin_switch(self) -> Button:
        return self.__begin_switch

    @property
    def end_switch(self) -> Button:
        return self.__end_switch

    @property
    def motor(self) -> Motor:
        return self.__motor
