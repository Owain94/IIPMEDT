from classes.Button import Button
from classes.Disk import Disk
from classes.Led import Led
from classes.Buzzer import Buzzer
from classes.Telephone import Telephone
from classes.User import User
from classes.State import State
from classes.Road import Road
from classes.Display import Display
from time import sleep
import RPi.GPIO as GPIO

# Other
road = Road(1, 1, [1, 2, 3, 4])  # road with 2 switches and a motor.
telephone = Telephone(1)  # Telephone with button input pin.
motor = road.motor  # Motor with input pins.
disk_products = Disk()  # Food disk with range.
arduino = disk_products.arduino  # Arduino
user = User()  # User.
state = State()  # Current state
buzzer = Buzzer(1.0, 1)  # Bell with output pin.

# Switches
switch_begin = road.begin_switch  # Begin switch input pin.
switch_end = road.end_switch  # End switch input pin.

# Buttons
button_start = Button(1)  # Start button input pin.
button_plus = Button(1)  # Plus button input pin.
button_done = Button(1)  # Done button input pin.
button_telephone = telephone.button  # Telephone button.

# Led's
led_start_red = Led(1)  # Start led red input pin.
led_plus_red = Led(1)  # Plus led red input pin.
led_plus_green = Led(1)  # Plus led green input pin.

# Displays
display_one = Display()
display_two = Display()


# de twee displays schoonmaken
def clear() -> None:
    display_one.clear()
    display_two.clear()

try:
    while True:
        #  STAP 2
        #  De state is 'initial' en de start button is ingedrukt.
        if state.is_state('initial') and button_start.is_pressed():
            state.current_state = 'button_start_pressed'

        #  STAP 1
        #  De state is 'initial'.
        elif state.is_state('initial'):
            if not led_start_red.thread_is_alive():
                led_start_red.blink_in_thread(1.0)

        #  STAP 4
        #  De state is 'button_start_pressed' en de telefoon knop
        #  is niet ingedrukt.
        elif state.is_state('button_start_pressed')\
                and not button_telephone.is_pressed():
            state.current_state = 'telephone_picked_up_for_first_time'

        #  STAP 3
        #  De state is 'button_start_pressed'
        elif state.is_state('button_start_pressed'):
            buzzer.buzz_in_thread()

        #  STAP 5
        #  De state is 'telephone_picked_up_for_first_time'
        elif state.is_state('telephone_picked_up_for_first_time'):
            state.current_state = 'telephone_first_track_played'
            telephone.play_track('welcome_track')  # todo audio file

        #  STAP 6
        #  De state is 'telephone_first_track_played' en de telefoon
        #  knop is ingedrukt.
        elif state.is_state('telephone_first_track_played')\
                and button_telephone.is_pressed():
            led_plus_red.blink_in_thread(1.0)
            while not button_done.is_pressed():
                if button_plus.is_pressed():
                    user.add_product()
                pass
            if button_done.is_pressed():
                state.current_state = 'products_selected'

        #  STAP 7
        #  De state is 'products_selected'
        elif state.is_state('products_selected'):
            motor.up(user.convert_score_to_motor(user.calculate_final_score(
                user.calculate_health_score(user.user_products),
                user.calculate_calorie_score(user.user_products))))
            state.current_state = 'telephone_feedback_first_score'

        #  STAP 8
        #  De state is 'telephone_feedpack_first_score'
        elif state.is_state('telephone_feedback_first_score'):
            state.current_state = 'first_feedback_track_played'
            telephone.play_track(user.determine_feedback_playback(
                user.calculate_health_score(user.user_products),
                user.calculate_calorie_score(user.user_products)))

        #  STAP todo stap nummer
        #  Hier wordt de state 'initial' en de displays worden gereset.
        else:
            state.reset_state()
            clear()

        #  De huidige status wordt geprint.
        print('Huidige status: ' + state.current_state)

        sleep(0.1)

#  Alles wordt opgeruimd.
except KeyboardInterrupt:
    GPIO.cleanup()
    clear()
