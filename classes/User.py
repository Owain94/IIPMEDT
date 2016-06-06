if __name__ == '__main__':
    from Disk import Disk
else:
    from classes.Disk import Disk




class User:
    """
    Klasse om bij te houden welke producten de gebruiker allemaal
    heeft toegevoegd
    """
    def __init__(self):
        """
        Code die wordt uitgevoerd bij het instantiëren van de klasse
        """
        self.__user_products = []

    def add_product(self) -> None:
        """
        Voeg een product toe aan de lijst met producten
        """
        self.__user_products.append(self.get_product_information())

    @staticmethod
    def calculate_calorie_score(products: list) -> float:
        """
        Reken totaal aantal caloriën uit van de gekozen producten

        :return: De kcal score als float
        """
        kcal = 0 
        for product_list in products:
            for product in product_list:
                kcal += product['kcal']

        return round(kcal / 80, 1)
        
    @staticmethod
    def calculate_health_score(products: list) -> float:
        """
        Reken gezondheidscijfer uit van de gekozen producten

        :return: De gezondheidswaarde score als float
        """
        score = 0
        count = 0 
        for product_list in products:
            for product in product_list:
                score += product['score']
                count += 1 

        return round((score / count) / 2, 1)
    
    @staticmethod
    def calculate_final_score(score: float, kcal_score: float) -> float:
        """
        Bereken totale score op basis van score en kcal score

        :param score: Gezondheidswaarde score als float
        :param kcal_score: Kcal score als float
        :return: De uiteindelijke score als float
        """
        return round((0.7 * kcal_score) + (0.3 * score), 1)

    @staticmethod
    def convert_score_to_motor(final_score: float) -> int:
        """
        Zet berekende score om in aantal motorstappen

        :param final_score: Uiteindelijke score als float
        :return: Het aantal stappen dat de motor moet draaien als int
        """
        return final_score * 100

    @staticmethod
    def determine_feedback_playback(score: float, kcal_score: float) -> str:
        """
        Zoek uit welk bestand er af gespeeld moet worden aan de hand van
        de scores

        :param score: Gezondheidswaarde score als float
        :param kcal_score: Kcal score als float
        :return: De track naam die afgespeeld moet worden als string
        """

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

        return track_name
            
    @staticmethod
    def get_product_information() -> list:
        """
        Haalt de live waarde van POT meter op en haalt het daarbij horende
        product op.

        :return: Alle producten als lijst
        """
        disk = Disk()
        li = [disk.get_product_by_index()]

        return li

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

    for i in range(10):
        user.add_product()

    health = user.calculate_health_score(user.user_products)
    calories = user.calculate_calorie_score(user.user_products)

    print("{}\n{}\n{}".format(health, calories,
                              user.calculate_final_score(health, calories)))

# Zorg ervoor dat de main functie niet wordt uitgevoerd als de klasse
# wordt geimporteerd
if __name__ == "__main__":
    main()
