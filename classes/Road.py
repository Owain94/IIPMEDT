if __name__ == '__main__':
    from sys import path

    path.append("..")

from classes.Button import Button
from classes.Motor import Motor
from util.Constants import Constants


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

        self.__const = Constants(max_steps=5000)

    def move_to_begin(self) -> None:
        """
        Blijf de motor draaien tot de begin positie is bereikt
        """
        while not self.__begin_switch.is_pressed():
            self.__motor.down()

        self.up(20)

    def move_a_quart(self, up: bool = True) -> None:
        """
        Verplaatst het 'poppertje' een kwart omhoog of omlaag.
        :param up: omhoog of omlaag als bool
        """
        quart = self.__const.max_steps / 4

        if up:
            self.up(quart)
        else:
            self.down(quart)

    def move_a_half(self, up: bool = True) -> None:
        """
        Verplaatst het 'poppertje' de helft omhoog of omlaag.
        :param up: omhoog of omlaag als bool
        """
        quart = self.__const.max_steps / 2

        if up:
            self.up(quart)
        else:
            self.down(quart)

    def move_a_three_quarter(self, up: bool = True) -> None:
        """
        Verplaatst het 'poppertje' drie kwart omhoog of omlaag.
        :param up: omhoog of omlaag als bool
        """
        quart = (self.__const.max_steps / 4) * 3

        if up:
            self.up(quart)
        else:
            self.down(quart)

    def move_to_end(self) -> None:
        """
        Blijf de motor draaien tot de eind positie is bereikt
        """
        while not self.__end_switch.is_pressed():
            self.__motor.up()

        self.down(20)

    def up(self, steps: int) -> None:
        """
        Beweeg het motortje omhoog met het aantal opgegeven stappen.
        :param steps: Het aantal stappen als int.
        """
        for step in range(steps):
            if not self.end_switch.is_pressed():
                self.__motor.up()
                pass
            else:
                self.down(20)
                break

    def down(self, steps: int) -> None:
        """
        Beweeg het motortje omhoog met het aantal opgegeven stappen.
        :param steps: Het aantal stappen als int.
        """
        for step in range(steps):
            if not self.begin_switch.is_pressed():
                self.__motor.down()
                pass
            else:
                self.up(20)
                break

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
