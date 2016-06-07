import os

if __name__ == '__main__':
    from sys import path
    path.append("..")

import subprocess
import time
from util.Constants import Constants
from xml.dom import minidom
from classes.Button import Button


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
        # Inladen van het xml bestand met de audio bestanden
        print(os.getcwd())

        self.__tracks = minidom.parse('../datafiles/tracks.xml')\
            .getElementsByTagName("track")
        self.__button = Button(input_pin)
        self.__butoon = None
        self.const = Constants(amount_per_second=4)

    def play_multiple_tracks(self, tracks: list) -> None:
        """
        Speel meerdere audio bestanden achter elkaar af

        :param tracks: De bestanden die afgespeeld moeten worden als lijst
        """
        # for track in tracks:
        #    self.play_track(track)
        [(self.play_track(track)) for track in tracks]

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

                for i in range(1, (duration * self.const.amount_per_second)):
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
                return track.getElementsByTagName("file")[0]\
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
                             .firstChild.data)

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
    telephone = Telephone(2)
    print(telephone.get_track_name('Wit_brood'))
    print(telephone.get_track_duration('Wit_brood'))

# Zorg ervoor dat de main functie niet wordt uitgevoerd als de klasse
# wordt geimporteerd
if __name__ == '__main__':
    main()
