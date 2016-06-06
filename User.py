from Disk import Disk
from Telephone import Telephone
from time import sleep

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

        :param product: Het toe te voegen product als string
        """
        self.__user_products.append(self.get_product_information())

    def calculate_calorie_score(self) -> float:
        """
        Reken totaal aantal caloriën uit van de gekozen producten
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
        
    def convert_score_to_motor(self, final_score: float) -> int:
        """
        Zet berekende score om in aantal motorstappen
        """
        
        aantal_stappen = final_score * 100
        
        return aantal_stappen
        
    def determine_feedback_playback(self, final_score: float): 
        track_name = ""
        if final_score < 4:
            track_name = ""
            
    
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
    user = User()

    for i in range(10):
        user.add_product()

    user.calculate_score()

if __name__ == "__main__":
    main()
