import subprocess
import time
from xml.dom import minidom
from util.Constants import Constants

if __name__ == '__main__':
    from Button import Button
else:
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
        document = minidom.parse('xml/tracks.xml')
        self.__tracks = document.getElementsByTagName("track")
        self.__button = Button(input_pin)
        self.const = Constants(amount_per_second=4)

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

                file = track.getElementsByTagName("file")[0].firstChild.data

                duration = int(track.getElementsByTagName("duration")[0].firstChild.data)

                process = subprocess.Popen("exec mpg321 " + file, stdout=subprocess.PIPE, shell=True)

                for i in range(1, (duration * self.const.amount_per_second)):
                    if self.__button.is_pressed():
                        break
                    time.sleep(1 / self.const.amount_per_second)
                    pass
                process.kill()

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
    print(telephone.play_multiple_tracks(['wit_brood', 'bruin_brood']))

# Zorg ervoor dat de main functie niet wordt uitgevoerd als de klasse
# wordt geimporteerd
if __name__ == '__main__':
    main()
