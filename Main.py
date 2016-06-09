from classes.Button import Button
from classes.Disk import Disk
from classes.Led import Led
from classes.Buzzer import Buzzer
from classes.Telephone import Telephone
from classes.User import User
from classes.State import State
from classes.Road import Road
from classes.Display import Display
from util.GPIOFuckUp import GPIOFuckUp
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# Other
road = Road(1, 1, [26, 19, 13, 6])  # road with 2 switches and a motor.
telephone = Telephone(23)  # Telephone with button input pin.
motor = road.motor  # Motor with input pins.
disk_products = Disk()  # Food disk with range.
arduino = disk_products.arduino  # Arduino
user = User()  # User.
state = State()  # Current state
buzzer = Buzzer(24)  # Bell with output pin.

# Switches
switch_begin = road.begin_switch  # Begin switch input pin.
switch_end = road.end_switch  # End switch input pin.

# Buttons
button_start = Button(21)  # Start button input pin.
button_plus = Button(5)  # Plus button input pin.
button_done = Button(4)  # Done button input pin.
button_telephone = telephone.button  # Telephone button.

# Led's
led_start_red = Led(12)  # Start led red input pin.
led_plus_red = Led(20)  # Plus led red input pin.
led_plus_green = Led(16)  # Plus led green input pin.

# Displays
display_one = Display(0x70)  # Eerste display
display_two = Display(0x71)  # Tweede display


# de twee displays schoonmaken
def clear() -> None:
    display_one.clear()
    display_two.clear()


# print de huidige status
def status(step) -> None:
    #  De huidige status wordt geprint.
    print('Stap: ' + str(step))
    print('Huidige status: ' + state.current_state)

# Alle GPIO pinnen worden op false gezet
GPIOFuckUp()

# Beide displays uitzetten
clear()

# zet het stapnummer
step = 0

try:
    while True:
        #  STAP 2
        #  De state is 'initial' en de start button is ingedrukt.
        if state.is_state('initial') and button_start.is_pressed():
            #  Zet het stapnummer
            step = 2
            #  Verander de state naar 'button_start_pressed'
            state.current_state = 'button_start_pressed'

        #  STAP 1
        #  De state is 'initial'.
        elif state.is_state('initial'):
            #  Zet het stapnummer
            step = 1
            #  Als het ledje nog niet knippert.
            if not led_start_red.thread_is_alive():
                #  laat het ledje knipperen voor 1 seconden.
                led_start_red.blink_in_thread(0.5)

        #  STAP 4
        #  De state is 'button_start_pressed' en de telefoon knop
        #  is niet ingedrukt.
        elif state.is_state('button_start_pressed')\
                and not button_telephone.is_pressed():
            #  Zet het stapnummer
            step = 4
            #  Verander de state naar 'telephone_picked_up_for_first_time'
            state.current_state = 'telephone_picked_up_for_first_time'

        #  STAP 3
        #  De state is 'button_start_pressed'
        elif state.is_state('button_start_pressed'):
            #  Zet het stapnummer
            step = 3
            #  Kijk of de buzzer thread bestaat
            if not buzzer.buzzer_is_alive():
                #  Speel de buzzer af in een thread
                buzzer.buzz_in_thread(0.5)

        #  STAP 5
        #  De state is 'telephone_picked_up_for_first_time'
        elif state.is_state('telephone_picked_up_for_first_time'):
            #  Zet het stapnummer
            step = 5
            #  Verander de state naar 'telephone_first_track_played'
            state.current_state = 'telephone_first_track_played'
            #  Even 2 seconden wachten voordat de audio af gaat spelen.
            sleep(2.0)
            #  Speel de track Ontvangsbericht.mp3 af.
            telephone.play_track('Ontvangsbericht')

        #  STAP 6
        #  De state is 'telephone_first_track_played' en de telefoon
        #  knop is ingedrukt.
        elif state.is_state('telephone_first_track_played')\
                and button_telephone.is_pressed():
            #  Zet het stapnummer
            step = 6
            #  Wanneer de klaar knop niet ingedrukt is
            while not button_done.is_pressed():
                #  Als de plus knop niet ingedrukt is
                if button_plus.is_pressed():
                    #  De groene led knippert voor feedback
                    if not led_plus_green.thread_is_alive():
                        led_plus_green.blink_in_thread(0.75)
                    #  Wordt het product toegevoegd aan de lijst met producten
                    user.add_product()
                #  De rode led knippert voor feedback
                elif not led_plus_red.thread_is_alive():
                    led_plus_red.blink_in_thread(0.5)
                #  Print de huidige status.
                status(step)
            #  Als de klaar knop ingedrukt wordt
            if button_done.is_pressed():
                #  Verander de status naar 'products_selected'
                state.current_state = 'products_selected'

        #  STAP 8
        #  De state is 'button_start_pressed' en de telefoon knop
        #  is niet ingedrukt.
        elif state.is_state('products_selected')\
                and not button_telephone.is_pressed():
            #  Zet het stapnummer
            step = 8
            #  Verander de state naar 'telephone_picked_up_for_first_time'
            state.current_state = 'give_score_to_the_user'

        #  STAP 7
        #  De state is 'button_start_pressed'
        elif state.is_state('products_selected'):
            #  Zet het stapnummer
            step = 7
            #  Kijk of de buzzer thread bestaat
            if not buzzer.buzzer_is_alive():
                #  Speel de buzzer af in een thread
                buzzer.buzz_in_thread(0.5)

        #  STAP 9
        #  De state is 'products_selected'
        elif state.is_state('give_score_to_the_user'):
            #  Wacht 2 seconden voordat de gebruiker de telefoon oppakt.
            sleep(2.0)
            #  Speel de lijst met producten af voor de gebruiker.
            telephone.play_multiple_tracks(
                telephone.prepare_track_list(user.user_products))
            #  Controleert of het de eerste keer is.
            if user.is_first_run():
                #  Zet het stapnummer
                step = 9
                #  Laat de score van de gebruiker op het eerste schermpje zien
                display_one.show_digit(user.calculate_final_score())
            else:
                #  Laat de score van de gebruiker op het eerste schermpje zien
                display_two.show_digit(user.calculate_final_score())
            #  Laat het 'poppertje' omhoog lopen
            #  todo is wegehaald voor prototype
            # road.up(user.convert_score_to_motor(user.calculate_final_score()))
            #  Verander de state naar 'ring_telephone_for_score'
            state.current_state = 'ring_telephone_for_score'

        #  STAP 11
        #  De state is 'button_start_pressed' en de telefoon knop
        #  is niet ingedrukt.
        elif state.is_state('ring_telephone_for_score')\
                and not button_telephone.is_pressed():
            #  Zet het stapnummer
            step = 11
            #  Verander de state naar 'telephone_feedback_first_score'
            state.current_state = 'telephone_feedback_score'

        #  STAP 10
        #  De state is 'button_start_pressed'
        elif state.is_state('ring_telephone_for_score'):
            #  Zet het stapnummer
            step = 10
            #  Kijk of de buzzer thread bestaat
            if not buzzer.buzzer_is_alive():
                #  Speel de buzzer af in een thread
                buzzer.buzz_in_thread(0.5)

        #  STAP 12
        #  De state is 'telephone_feedback_first_score'
        elif state.is_state('telephone_feedback_score'):
            #  Zet het stapnummer
            step = 12
            #  Verander de state naar 'telephone_feedback_score'
            state.current_state = 'telephone_feedback_score'
            #  Wacht 2 seconden voor het afspelen van de telefoon
            sleep(2.0)
            #  Speel de bijpassende feedback af op de telefoon.
            telephone.play_track(user.determine_feedback_playback())
            #  Wacht 2 seconden voor het bewegen naar de terug positie
            sleep(2.0)
            #  Het 'poppertje' beweegt zich terug naar de home positie.
            #  todo weggehaald voor protoype
            # road.move_to_begin()
            #  De gekozen productenlijst wordt geleegd.
            user.reset_products()
            #  Geef door dat de eerste keer geeindigd is.
            user.second_run()

        #  Hier wordt de state 'initial' en de displays worden gereset.
        # else:
            #  Reset de state naar 'initial'
            # state.reset_state()
            #  Zet alle display ledjes uit.
            # clear()

        #  Print de huidige status.
        status(step)

        #  De loop wordt 10 per seconden afgespeeld
        sleep(0.1)

#  Alles wordt opgeruimd.
except KeyboardInterrupt:
    #  Haalt alle stroom van de pinnen af
    GPIO.cleanup()
    #  Zet alle display ledjes uit.
    clear()
