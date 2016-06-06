if __name__ == '__main__':
    from Button import Button
    from Motor import Motor
else:
    from classes.Button import Button
    from classes.Motor import Motor


class Road:
    """
    Klasse om displays aan te sturen
    """
    def __init__(self,
                 begin_switch_input_pin: int,
                 end_switch_input_pin: int,
                 motor_input_pins: list
                 ) -> None:
        """
        Code die wordt uitgevoerd bij het instantiëren van de klasse

        :param begin_switch_input_pin: De GPIO pins van de begin switch,
                                       als int
        :param end_switch_input_pin: De GPIO pins van de eind switch, als int
        :param motor_input_pins: De GPIO pins die de motor gebruikt als lijst
        """
        self.__begin_switch = Button(begin_switch_input_pin)
        self.__end_switch = Button(end_switch_input_pin)
        self.__motor = Motor(motor_input_pins)

    def move_to_begin(self) -> None:
        """
        Blijf de motor draaien tot de begin positie is bereikt
        """
        while not self.__begin_switch.is_pressed():
            self.__motor.down(1)

        self.__motor.up(20)

    def move_to_end(self) -> None:
        """
        Blijf de motor draaien tot de eind positie is bereikt
        """
        while not self.__end_switch.is_pressed():
            self.__motor.up(1)

        self.motor.down(20)

    @property
    def begin_switch(self) -> Button:
        """
        Getter voor de begin switch

        :return: Instantie van de button klasse
        """
        return self.__begin_switch

    @property
    def end_switch(self) -> Button:
        """
        Getter voor de eind switch

        :return: Instantie van de button klasse
        """
        return self.__end_switch

    @property
    def motor(self) -> Motor:
        """
        Getter voor de motor

        :return: Instantie van de motor klasse
        """
        return self.__motor
