from classes.Button import Button
from classes.Disk import Disk
from classes.Led import Led
from classes.Telephone import Telephone
from classes.User import User
from classes.State import State
from classes.Road import Road
from classes.Display import Display
from util.GPIOFuckUp import GPIOFuckUp
from time import sleep
import RPi.GPIO as GPIO
import os

GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# Displays
display_one = Display(0x71)  # Eerste display
display_two = Display(0x70)  # Tweede display


# de twee displays schoonmaken
def clear_displays() -> None:
    display_one.clear()
    display_two.clear()


# Beide displays uitzetten
clear_displays()

# Other
road = Road(17, 22, [6, 13, 19, 26])  # road with 2 switches and a motor.
telephone = Telephone(23)  # Telephone with button input pin.
motor = road.motor  # Motor with input pins.
disk_products = Disk()  # Food disk with range.
arduino = disk_products.arduino  # Arduino
user = User()  # User.
state = State()  # Current state

# Switches
switch_begin = road.begin_switch  # Begin switch input pin.
switch_end = road.end_switch  # End switch input pin.

# Buttons
button_start = Button(21)  # Start button input pin.
button_plus = Button(5)  # Plus button input pin.
button_done = Button(4)  # Done button input pin.
button_telephone = telephone.button  # Telephone button.
button_off = Button(27)  # Off button input pin.

# Led's
led_start_red = Led(12)  # Start led red input pin.
led_plus_red = Led(16)  # Plus led red input pin.
led_plus_green = Led(20)  # Plus led green input pin.

# Alle GPIO pinnen worden op false gezet
GPIOFuckUp()

try:
    #  Zolang de uitknop niet ingedrukt wordt,
    #  wordt onderstaande code uitgevoerd.
    while not button_off.is_pressed():
        #  STAP 2
        #  De state is 'initial' en de start button is ingedrukt.
        if state.is_state('initial') and button_start.is_pressed():
            #  Zet het stapnummer
            state.step = 2
            #  Verander de state naar 'button_start_pressed'
            state.current_state = 'button_start_pressed'

        # STAP 1
        #  De state is 'initial'.
        elif state.is_state('initial'):
            #  Zet het stapnummer
            state.step = 1
            #  Als het ledje nog niet knippert.
            if not led_start_red.thread_is_alive():
                #  laat het ledje knipperen voor 1 seconden.
                led_start_red.blink_in_thread(0.5)

        # STAP 4
        #  De state is 'button_start_pressed' en de telefoon knop
        #  is niet ingedrukt.
        elif state.is_state('button_start_pressed') \
                and not button_telephone.is_pressed():
            #  Zet het stapnummer
            state.step = 4
            #  Verander de state naar 'telephone_picked_up_for_first_time'
            state.current_state = 'telephone_picked_up_for_first_time'

        # STAP 3
        #  De state is 'button_start_pressed'
        elif state.is_state('button_start_pressed'):
            #  Zet het stapnummer
            state.step = 3
            #  Kijkt of de ringtone thread bestaat
            if not telephone.play_ringtone_thread_alive():
                #  Speelt de ringtone af in een aparte thread
                telephone.play_ringtone_in_thread()

        # STAP 5
        #  De state is 'telephone_picked_up_for_first_time'
        elif state.is_state('telephone_picked_up_for_first_time'):
            #  Zet het stapnummer
            state.step = 5
            #  Verander de state naar 'telephone_first_track_played'
            state.current_state = 'telephone_first_track_played'
            #  Even 2 seconden wachten voordat de audio af gaat spelen.
            sleep(2.0)
            #  Speel de track Ontvangsbericht.mp3 af.
            telephone.play_track('Ontvangsbericht')

        # STAP 6
        #  De state is 'telephone_first_track_played' en de telefoon
        #  knop is ingedrukt.
        elif state.is_state('telephone_first_track_played') \
                and button_telephone.is_pressed():
            #  Zet het stapnummer
            state.step = 6

            #  Wanneer de klaar knop niet ingedrukt is
            while not button_done.is_pressed():
                #  potential
                potential = disk_products.get_serial()
                #  Als de plus knop niet ingedrukt is
                if button_plus.is_pressed():
                    if not button_plus.is_fake_pressed():
                        #  Wordt het product toegevoegd aan
                        #  de lijst met producten
                        if not user.add_product_thread_is_alive():
                            user.add_product_in_thread(potential)
                            #  De groene led knippert voor feedback
                            if not led_plus_green.thread_is_alive():
                                led_plus_green.blink_in_thread(0.75)
                        # Zet de fake button op true
                        button_plus.fake_pressed = True
                # De rode led knippert voor feedback
                elif not led_plus_red.thread_is_alive():
                    led_plus_red.blink_in_thread(0.5)
                    #  Zet de fake button op false
                    button_plus.fake_pressed = False
                # Print de huidige status.
                state.status()

            # Als de klaar knop ingedrukt wordt
            if button_done.is_pressed():
                #  Verander de status naar 'products_selected'
                state.current_state = 'products_selected'

        # De state is 'telephone_first_track_played'.
        elif state.is_state('telephone_first_track_played'):
            #  Controleert na 10 seconden of de telefoon terug gehangen is.
            if state.is_count():
                #  Speelt de mp3 af die vertelt dat de gebruiker de telefoon
                #  moet terug hangen.
                telephone.play_track('Telefoon_terugleg_bericht')
                #  de count wordt reset voor de zekerheid.
                state.reset_count()
            else:
                #  De count wordt opgeteld.
                state.count_up()

        # STAP 8
        #  De state is 'button_start_pressed' en de telefoon knop
        #  is niet ingedrukt.
        elif state.is_state('products_selected') \
                and not button_telephone.is_pressed():
            #  Zet het stapnummer
            state.step = 8
            #  Verander de state naar 'telephone_picked_up_for_first_time'
            state.current_state = 'give_score_to_the_user'

        # STAP 7
        #  De state is 'button_start_pressed'
        elif state.is_state('products_selected'):
            #  Zet het stapnummer
            state.step = 7
            #  Kijkt of de ringtone thread bestaat
            if not telephone.play_ringtone_thread_alive():
                #  Speelt de ringtone af in een aparte thread
                telephone.play_ringtone_in_thread()

        # STAP 9
        #  De state is 'products_selected'
        elif state.is_state('give_score_to_the_user'):
            #  Wacht 2 seconden voordat de gebruiker de telefoon oppakt.
            sleep(2.0)
            #  Controleert of het de eerst run is.
            if user.is_first_run():
                #  Zet het stapnummer
                state.step = 9
                #  Laat de score van de gebruiker op het eerste schermpje zien
                if not user.added_zero_products():
                    # toont het cijfer.
                    display_one.show_digit(user.calculate_final_score())
                else:
                    # toont het cijfer 0.0
                    display_one.show_digit(0.0)
            else:
                #  Laat de score van de gebruiker op het eerste schermpje zien
                if not user.added_zero_products():
                    # toont het cijfer.
                    display_two.show_digit(user.calculate_final_score())
                else:
                    # toont het cijfer 0.0
                    display_two.show_digit(0.0)
            # Controleert of de gebruiker 0 producten toegevoegd heeft.

            # todo debugging
            print("Lijst is leeg: " + str(user.added_zero_products()))

            if not user.added_zero_products():
                # todo
                print(telephone.prepare_track_list(user.user_products))
                #  Speel de lijst met producten af voor de gebruiker.
                telephone.play_multiple_tracks(
                    telephone.prepare_track_list(user.user_products))
                # Laat het 'poppertje' omhoog lopen
                road.up(user.convert_score_to_motor(user.calculate_final_score()))
            #  Verander de state naar 'ring_telephone_for_score'
            state.current_state = 'ring_telephone_for_score'

        # STAP 11
        #  De state is 'button_start_pressed' en de telefoon knop
        #  is niet ingedrukt.
        elif state.is_state('ring_telephone_for_score') \
                and not button_telephone.is_pressed():
            #  Zet het stapnummer
            state.step = 11
            #  Verander de state naar 'telephone_feedback_first_score'
            state.current_state = 'telephone_feedback_score'

        # STAP 10
        #  De state is 'button_start_pressed'
        elif state.is_state('ring_telephone_for_score'):
            #  Zet het stapnummer
            state.step = 10
            #  Kijkt of de ringtone thread bestaat
            if not telephone.play_ringtone_thread_alive():
                #  Speelt de ringtone af in een aparte thread
                telephone.play_ringtone_in_thread()

        # STAP 12
        #  De state is 'telephone_feedback_first_score'
        elif state.is_state('telephone_feedback_score'):
            #  Zet het stapnummer
            state.step = 12
            #  Verander de state als de gebruiker voor de eerste keer hier is.
            if user.is_first_run():
                #  Verander de state naar 'telephone_feedback_score'
                state.current_state = 'telephone_first_track_played'
            else:
                #  Verader de state naar 'both_breakfast_filled_in'
                state.current_state = 'both_breakfast_filled_in'
            # Wacht 2 seconden voor het afspelen van de telefoon
            sleep(2.0)

            if user.is_first_run() and user.breakfast_is_perfect(
                    user.determine_feedback_playback()):
                # De smiley wordt op het tweede scherm getoond.
                display_two.show_smiley()

            if not user.added_zero_products():
                #  Controleert of het eerste ontbijt perfect is.
                if user.breakfast_is_perfect(
                        user.determine_feedback_playback()):
                    #  Veranderd de state naar de eind state.
                    state.current_state = 'both_breakfast_filled_in'
                #  Speel de bijpassende feedback af op de telefoon.
                telephone.play_track(user.determine_feedback_playback())
            else:
                #  Op basis van de run wordt de juiste audio ingeladen.
                if user.is_first_run():
                    #  Speelt een audio track af over slecht ontbijten.
                    telephone.play_track('Ontbijt_vergeten_eerste_keer')
                else:
                    #  Speelt een audio track af over slecht ontbijten.
                    telephone.play_track('Ontbijt_vergeten_tweede_keer')

            # Wacht 2 seconden voor het bewegen naar de terug positie
            sleep(2.0)
            #  Het 'poppertje' beweegt zich terug naar de home positie.
            road.move_to_begin()
            #  De gekozen productenlijst wordt geleegd.
            user.reset_products()
            #  Geef door dat de eerste keer geeindigd is.
            user.second_run()

        # Hier wordt de state 'initial' en de displays worden gereset.
        elif state.is_state('both_breakfast_filled_in'):
            #  Eind bericht
            telephone.play_track('Eind_bericht')
            #  Reset de state naar 'initial'
            state.reset_state()
            #  Reset de stap naar 0
            state.reset_step()
            #  Reset first run
            user.reset_run()
            #  Zet alle display ledjes uit.
            clear_displays()

        # Print de huidige status.
        state.status()

        #  De loop wordt 10 per seconden afgespeeld
        sleep(0.1)

    #  Haalt alle stroom van de pinnen af
    GPIO.cleanup()
    # Alle GPIO pinnen worden op false gezet
    GPIOFuckUp()
    #  Zet alle display ledjes uit.
    clear_displays()

    # De raspberry pi wordt uitgezet als de uitknop wordt ingedrukt.
    os.system("/sbin/shutdown -h now")

# Alles wordt opgeruimd.
except KeyboardInterrupt:
    #  Haalt alle stroom van de pinnen af
    GPIO.cleanup()
    # Alle GPIO pinnen worden op false gezet
    GPIOFuckUp()
    #  Zet alle display ledjes uit.
    clear_displays()
