if __name__ == '__main__':
    from sys import path

    path.append("..")

import subprocess
import time
import os
from util.Constants import Constants
from util.Helpers import prefix
from xml.dom import minidom
from classes.Button import Button
from math import ceil
from threading import Thread, ThreadError
from slugify import slugify


class Telephone:
    """
    Klasse om audio bestanden af te spelen
    """

    def __init__(self, input_pin: int) -> None:
        """
        Code die wordt uitgevoerd bij het instantiëren van de klasse

        :param input_pin: De GPIO pin die wordt gebruikt op de raspberry
                          om te kijken of de hoorn is opgenomen of niet,
                          als int
        """
        self.__tracks = minidom.parse(prefix() + 'datafiles/tracks.xml') \
            .getElementsByTagName("track")
        self.__button = Button(input_pin)
        self.__ringtone_thread = None
        self.const = Constants(
            amount_per_second=4
        )

    @staticmethod
    def play_ringtone() -> None:
        """
        Speel de ringtone af.
        """
        os.system('mpg321 -q ' + prefix() + 'audio/Tring.mp3')

    def play_ringtone_in_thread(self) -> None:
        """
        Speel de ringtone af in een thread.
        """
        self.__ringtone_thread = Thread(target=self.play_ringtone)
        self.__ringtone_thread.start()

    def play_ringtone_thread_alive(self) -> bool:
        """
        Haal de thread status op van de ringtone.

        :return: Of de ringtone actief is of niet als boolean.
        """
        try:
            return self.__ringtone_thread.is_alive()
        except ThreadError as e:
            print("Exception (Telephone, play_ringtone_thread_alive: {0})"
                  .format(e))
            return False
        except AttributeError as e:
            print("Exception (Telephone, play_ringtone_thread_alive: {0})"
                  .format(e))
            return False

    def play_multiple_tracks(self, tracks: list) -> None:
        """
        Speel meerdere audio bestanden achter elkaar af

        :param tracks: De bestanden die afgespeeld moeten worden als lijst
        """
        for track in tracks:
            self.play_track(track)

    def play_track(self, track_name: str) -> None:
        """
        Speel een audio track af in een apart process zodat er
        tegelijkertijd andere code kan worden gedraaid

        :param track_name: De track die moet worden afgespeeld als string
        """
        for track in self.__tracks:
            if track.getAttribute('product') == track_name:

                file = self.get_track_name(track_name)

                duration = self.get_track_duration(track_name)

                process = subprocess.Popen("exec mpg321 " + file,
                                           stdout=subprocess.PIPE,
                                           shell=True)

                for i in range(1,
                               ceil(duration * self.const.amount_per_second)):
                    if self.__button.is_pressed():
                        break
                    time.sleep(1 / self.const.amount_per_second)
                    pass
                process.kill()

    def get_track_name(self, key: str) -> str:
        """
        Krijg de locatie naar een audio bestand aan de hand van een naam

        :param key: naam om op te zoeken in het xml bestand
        :return: Path naar het audio bestand als string
        """
        for track in self.__tracks:
            if track.getAttribute('product') == key:
                return track.getElementsByTagName("file")[0] \
                    .firstChild.data

    def get_track_duration(self, key: str) -> float:
        """
        Krijg de duratie van een audio bestand aan de hand van een naam

        :param key: naam om op te zoeken in het xml bestand
        :return: Duratie van het audio bestand als float
        """
        for track in self.__tracks:
            if track.getAttribute('product') == key:
                return float(track.getElementsByTagName("duration")[0]
                             .firstChild.data) + 0.5

    @staticmethod
    def prepare_track_list(user_products: list) -> list:
        """
        Geef een lijst met tracks terug op basis van alle producten die de
        gebruiker heeft toegevoegd

        :param user_products: Alle toegevoegde producten
        :return: Alle tracks die afgespreeld moeten worden als lijst
        """
        tracks = []
        items = {}

        for product_list in user_products:
            for product in product_list:
                product_name = slugify(product['name'], separator="_")
                product_name = product_name[0].title() + product_name[1:]

                try:
                    items[product_name] = int(items[product_name]) + 1
                except KeyError as e:
                    print("Exception (Telephone, prepare_track_list: {0})"
                          .format(e))
                    items[product_name] = 1

        tracks.append('Gekozen')

        for item in items:
            if items[item] > 1:
                tracks.append(str(items[item]) + "x")
            else:
                tracks.append("1x")
            tracks.append(item)

        return tracks

    def play_breakfast(self, user_products: list) -> None:
        tracks = self.prepare_track_list(user_products)

        # Dit is puur een test om te zien wat er in de lijst zit
        print('\n'.join(map(str, tracks)))

    @property
    def button(self) -> Button:
        """
        Getter voor de knop van de telefoon

        :return: Instantie van de button klasse
        """
        return self.__button


def main() -> None:
    """
    Code om de klasse te testen, deze code wordt niet uitgevoerd als de
    klasse in een ander bestand wordt geimporteerd!
    """
    li = [
        [
            {
                'name': "Wit_brood",
            }
        ],
        [
            {
                'name': "Wit_brood",
            }
        ],
        [
            {
                'name': "Wit_brood",
            }
        ],
        [
            {
                'name': "Wit_brood",
            }
        ],
        [
            {
                'name': "bruin_brood",
            }
        ],
    ]

    telephone = Telephone(23)
    telephone.play_multiple_tracks(['Bruin_brood', 'Bruin_brood'])
    telephone.play_breakfast(li)


# Zorg ervoor dat de main functie niet wordt uitgevoerd als de klasse
# wordt geimporteerd
if __name__ == '__main__':
    main()
