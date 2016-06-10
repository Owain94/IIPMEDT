class Strings:
    def __init__(self, string: str):
        self.string = string

    def fix_string(self) -> str:
        return self.string.replace(', ', '_').replace(' en ', '_')


def main() -> None:
    """
    Code om de klasse te testen, deze code wordt niet uitgevoerd als de
    klasse in een ander bestand wordt geimporteerd!
    """
    string = Strings('Koffie, melk en sugar')
    print(string.fix_string())

# Zorg ervoor dat de main functie niet wordt uitgevoerd als de klasse
# wordt geimporteerd
if __name__ == '__main__':
    main()
