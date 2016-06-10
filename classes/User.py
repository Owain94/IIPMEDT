if __name__ == '__main__':
    from sys import path

    path.append("..")

from classes.Disk import Disk
from threading import Thread


class User:
    """
    Klasse om bij te houden welke producten de gebruiker allemaal
    heeft toegevoegd
    """

    def __init__(self):
        """
        Code die wordt uitgevoerd bij het instantiëren van de klasse
        """
        # Lijst voor alle gekozen producten
        self.__user_products = []
        # Of het de eerste keer is dat de gebruiker een ontbijt samen stelt.
        self.__first_run = True
        self.__add_thread = None
        self.__disk = Disk()

    def reset_run(self) -> None:
        """
        Reset de first run.
        """
        self.__first_run = True

    def second_run(self) -> None:
        """
        Met deze methode kan er worden opgegeven dat de gebruiker
        zijn 2e ontbijt opgeeft.
        """
        self.__first_run = False

    def added_zero_products(self) -> bool:
        return len(self.user_products) is 0

    def is_first_run(self) -> bool:
        """
        Met deze methode kan er worden uitgelezen of de gebruiker
        zijn eerste ontbijt invoert.

        :return: Of het de eerste keer is al boolean
        """
        return self.__first_run

    def add_product(self, potential: int) -> None:
        """
        Voeg een product toe aan de lijst met producten
        :param potential: De potential wordt meegegeven
        """
        self.__user_products.append(self.get_product_information(potential))

    def add_product_thread_is_alive(self) -> bool:
        # noinspection PyBroadException
        try:
            return self.__add_thread.is_alive()
        except:
            return False

    def add_product_in_thread(self, potential: int):
        self.__add_thread = Thread(target=self.add_product, args=(potential,))
        self.__add_thread.start()

    def reset_products(self) -> None:
        """
        Leegt de producten lijst.
        """
        self.__user_products = []

    @staticmethod
    def calculate_calorie_score(products: list) -> float:
        """
        Reken totaal aantal caloriën uit van de gekozen producten

        :param products: Een lijst met gekozen producten
        :return: De kcal score als float
        """
        kcal = 0
        for product_list in products:
            for product in product_list:
                kcal += float(product['kcal'])

        if kcal < 300:
            kcal /= 66.7
        elif 300 < kcal < 400:
            kcal = ((kcal - 300) / 100) + 4.5
        elif 400 < kcal < 800:
            kcal /= 88.9
        else:
            kcal = 1.0

        return round(kcal, 1)

    @staticmethod
    def calculate_health_score(products: list) -> float:
        """
        Reken gezondheidscijfer uit van de gekozen producten

        :param products: productenlijst
        :return: De gezondheidswaarde score als float
        """
        score = 0
        count = 0
        for product_list in products:
            for product in product_list:
                score += float(product['score'])
                count += 1

        return round((score / count) / 2, 1)

    def calculate_final_score(self) -> float:
        """
        Bereken totale score op basis van score en kcal score

        :return: De uiteindelijke score als float
        """
        score = self.calculate_health_score(self.user_products)
        kcal_score = self.calculate_calorie_score(self.user_products)

        return round((0.7 * kcal_score) + (0.3 * score), 1)

    def calculate_display_score(self) -> float:
        kcal = self.calculate_calorie_score(self.user_products)
        health_score = self.calculate_health_score(self.user_products)

        if kcal < 4.5:
            kcal_score = kcal
        elif 4.5 < kcal < 5.5:
            kcal_score = kcal * 2
        elif 5.5 < kcal < 10:
            minus = kcal - 5
            kcal_score = 5 - minus
        else:
            kcal_score = 1.0

        return round((0.7 * kcal_score) + (0.3 * (health_score * 2)), 1)

    @staticmethod
    def convert_score_to_motor(final_score: float) -> int:
        """
        Zet berekende score om in aantal motorstappen

        :param final_score: Uiteindelijke score als float
        :return: Het aantal stappen dat de motor moet draaien als int
        """
        # todo een juiste berekening
        return int(round(final_score * 100))

    def determine_feedback_playback(self) -> str:
        """
        Zoek uit welk bestand er af gespeeld moet worden aan de hand van
        de scores

        :return: De track naam die afgespeeld moet worden als string
        """

        score = self.calculate_health_score(self.user_products)
        kcal_score = self.calculate_calorie_score(self.user_products)

        if score < 3.5:
            if kcal_score > 6:
                track_name = "Ontbijt_lage_gezondheidswaarde_teveel_eten"
            elif kcal_score < 4:
                track_name = "Ontbijt_lage_gezondheidswaarde_weinig_eten"
            else:
                track_name = "Ontbijt_lage_gezondheidswaarde_genoeg_eten"
        else:
            if kcal_score > 6:
                track_name = "Ontbijt_goede_gezondheidswaarde_teveel_eten"
            elif kcal_score < 4:
                track_name = "Ontbijt_goede_gezondheidswaarde_weinig_eten"
            else:
                track_name = "Ontbijt_perfect"

        if self.is_first_run() and not self.breakfast_is_perfect(track_name):
            track_name += "_eerste_keer"
        elif not self.is_first_run() and not self.breakfast_is_perfect(
                track_name):
            track_name += "_tweede_keer"

        return track_name

    @staticmethod
    def breakfast_is_perfect(track_name: str) -> bool:
        """
        Controleert of het ontbijt perfect is en geeft dit terug als boolean.

        :param track_name: De naam van de track zonder .mp3
        :return: True of False
        """
        return track_name is "Ontbijt_perfect"

    def get_product_information(self, potential: int) -> list:
        """
        Haalt de live waarde van POT meter op en haalt het daarbij horende
        product op.

        :param potential: De potential wordt meegegeven
        :return: Alle producten als lijst
        """
        return [self.__disk.get_product_by_index(potential)]

    @property
    def user_products(self) -> list:
        """
        Lijst met alle producten van de gebruiker.

        :return: Producten van de gebruiker als lijst
        """
        return self.__user_products


def main() -> None:
    """
    Code om de klasse te testen, deze code wordt niet uitgevoerd als de
    klasse in een ander bestand wordt geimporteerd!
    """
    user = User()

    # for i in range(10):
    #    user.add_product()
    [(user.add_product(250)) for _ in range(10)]

    health = user.calculate_health_score(user.user_products)
    calories = user.calculate_calorie_score(user.user_products)

    print("{}\n{}\n{}".format(health, calories,
                              user.calculate_final_score()))


# Zorg ervoor dat de main functie niet wordt uitgevoerd als de klasse
# wordt geimporteerd
if __name__ == "__main__":
    main()
