import subprocess
import time
from xml.dom import minidom
#from Button import Button


class Telephone:
    def __init__(self, input_pin: int) -> None:
        document = minidom.parse('xml/tracks.xml')
        self.__tracks = document.getElementsByTagName("track")
        #self.__button = Button(input_pin)
        self.amount_per_second = 4

    def play_multiple_tracks(self, tracks: list) -> None:
        for track in tracks:
            self.play_track(track)

    def play_track(self, track_name: str) -> None:
        for track in self.__tracks:
            if track.getAttribute('product') == track_name:

                file = track.getElementsByTagName("file")[0].firstChild.data

                duration = int(track.getElementsByTagName("duration")[0].firstChild.data)

                process = subprocess.Popen("exec mpg321 " + file, stdout=subprocess.PIPE, shell=True)

                for i in range(1, (duration * self.amount_per_second)):
                    #if self.__button.is_pressed():
                    if False:
                        break
                    time.sleep(1 / self.amount_per_second)
                    pass
                process.kill()


def main() -> None:
    telephone = Telephone(2)
    print(telephone.play_multiple_tracks(['wit_brood', 'bruin_brood']))

if __name__ == '__main__':
    main()
