from Button import Button
from Disk import Disk
from Arduino import Arduino
from Led import Led
from Buzzer import Buzzer
from Motor import Motor
from Telephone import Telephone
from User import User
from State import State
from time import sleep

# todo all pins

telephone = Telephone(1)  # Telephone with button input pin.

# begin_switch = Button(1)  # Begin switch input pin.
# end_switch = Button(1)  # End switch input pin.
start_button = Button(3)  # Start button input pin.
# plus_button = Button(1)  # Plus button input pin.
# done_button = Button(1)  # Done button input pin.
telephone_button = telephone.button  # Telephone button.

start_led_red = Led(2)  # Start led red input pin.
# start_led_green = Led(1)  # Start led green input pin.
# plus_led_red = Led(1)  # Plus led red input pin.
# plus_led_green = Led(1)  # Plus led green input pin.

# food_disk = Disk(1024)  # Food disk with range.
# arduino = Arduino()  # Arduino
# motor = Motor([1, 2, 3, 4])  # Motor with input pins.
# user = User()  # User.
state = State()  # Current state
# bell = Bell(1)  # Bell with output pin.

while True:
    if state.is_state('initial') and start_button.is_pressed():
        state.current_state = 'start_button_pressed'  # updating current state.

    elif state.is_state('initial'):
        if not start_led_red.thread_is_alive():
            start_led_red.blink_in_thread(1.0)

    # elif state.is_state('start_button_pressed') and not telephone_button.is_pressed():
    #     state.current_state = 'telephone_picked_up_for_first_time'
    #
    # elif state.is_state('start_button_pressed'):
    #     bell.ring_in_thread(1.0)
    #
    # elif state.is_state('telephone_picked_up_for_first_time'):
    #     state.current_state = 'telephone_first_track_played'
    #     telephone.play_track('eerste_track')  # todo audio file
    #
    # elif state.is_state('telephone_first_track_played') and telephone_button.is_pressed():
    #     plus_led_red.blink_in_thread(1.0)  # green led blinking for 1 second.

    # else:
    #     state.reset_state()

    sleep(0.1)
