from Disk import Disk


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

    def calculate_calorie_score(self) -> float:
        """
        Reken totaal aantal caloriën uit van de gekozen producten

        :return: De kcal score
        """
        kcal = 0 
        for product_list in self.__user_products:
            for product in product_list:
                kcal += product['kcal']

        kcal_score = kcal / 80

        round(kcal_score, 1)

        return kcal_score
        
    def calculate_health_score(self) -> float: 
        """
        Reken gezondheidscijfer uit van de gekozen producten

        :return: De gezondheidswaarde score
        """
        score = 0
        count = 0 
        for product_list in self.__user_products:
            for product in product_list:
                score += product['score']
                count += 1 
                
        score = (score / count) / 2
        
        round(score, 1)

        return score
    
    @staticmethod
    def calculate_final_score(score: float, kcal_score: float) -> float:
        """
        Bereken totale score op basis van score en kcal score

        :param score: Gezondheidswaarde score
        :param kcal_score: Kcal score
        :return: De uiteindelijke score
        """
        """
        """
        
        final_score = (0.7 * kcal_score) + (0.3 * score)
        
        round(final_score, 1)
        
        return final_score

    @staticmethod
    def convert_score_to_motor(final_score: float) -> int:
        """
        Zet berekende score om in aantal motorstappen

        :param final_score: Uiteindelijke score
        :return: Het aantal stappen dat de motor moet draaien
        """
        aantal_stappen = final_score * 100

        return aantal_stappen

    @staticmethod
    def determine_feedback_playback(score: float, kcal_score: float) -> str:
        """
        Zoek uit welk bestand er af gespeeld moet worden aan de hand van
        de scores

        :param score: Gezondheidswaarde score
        :param kcal_score: Kcal score
        :return: De track naam die afgespeeld moet worden
        """
        track_name = ""
        if score < 3.5 and kcal_score > 6:
            track_name = "Ontbijt_lage_gezondheidswaarde_teveel_eten"
        
        elif score < 3.5 and kcal_score < 4:
            track_name = "Ontbijt_lage_gezondheidswaarde_weinig_eten"
        
        elif score < 3.5 and (4.5 < kcal_score < 5.5):
            track_name = "Ontbijt_lage_gezondheidswaarde_genoeg_eten"
            
        elif score > 3.5 and kcal_score > 6:
            track_name = "Ontbijt_goede_gezondheidswaarde_teveel_eten"
            
        elif score > 3.5 and kcal_score < 4:
            track_name = "Ontbijt_goede_gezondheidswaarde_weinig_eten"
            
        elif (score > 4.5) and (4.5 < kcal_score < 5.5):
            track_name = "Ontbijt_perfect"

        return track_name
            
    @staticmethod
    def get_product_information() -> list:
        """
        Haalt de live waarde van POT meter op en haalt het daarbij horende
        product op.

        :return: list met alle producten
        """
        li = []

        disk = Disk()
        li.append(disk.get_product_by_index())

        return li

    @property
    def user_products(self) -> list:
        """
        Lijst met alle producten van de gebruiker.

        :return: list met producten
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

    user.calculate_health_score()
    user.calculate_calorie_score()
    user.calculate_final_score()

# Zorg ervoor dat de main functie niet wordt uitgevoerd als de klasse
# wordt geimporteerd
if __name__ == "__main__":
    main()
