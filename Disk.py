from xml.dom import minidom


class Disk:
    def __init__(self, max_index: int) -> None:
        self._max = max_index
        document = minidom.parse('xml/products.xml')

        self._products = document.getElementsByTagName("product")
        self._disk_range = round(self._max / len(self._products), 2)
        self._product_count = len(self._products)

    def get_product_index(self, potential: int) -> int:
        for i in range(0, self._product_count):
            if (potential >= i * self._disk_range) and (potential <= ((i + 1) * self._disk_range)):
                return i

    def get_by_key(self, key: str, potential: int) -> str:
        index = self.get_product_index(potential)
        return self._products[index].getElementsByTagName(key)[0].firstChild.data

    def get_product_name_by_index(self, potential: int) -> str:
        return self.get_by_key('name', potential)

    def get_product_score_by_index(self, potential: int) -> str:
        return self.get_by_key('score', potential)

    def get_product_kcal_by_index(self, potential: int) -> str:
        return self.get_by_key('kcal', potential)

    def get_product_sugar_by_index(self, potential: int) -> str:
        return self.get_by_key('sugar', potential)

    def get_product_fat_by_index(self, potential: int) -> str:
        return self.get_by_key('fat', potential)

    @property
    def products(self) -> list:
        return self._products

    @property
    def disk_range(self) -> float:
        return self._disk_range

    @property
    def product_count(self) -> int:
        return self._product_count


def main() -> None:
    disk = Disk(1024)
    print(disk.get_product_name_by_index(250))
    print(disk.get_product_score_by_index(250))
    print(disk.get_product_kcal_by_index(250))
    print(disk.get_product_sugar_by_index(250))
    print(disk.get_product_fat_by_index(250))

if __name__ == '__main__':
    main()
