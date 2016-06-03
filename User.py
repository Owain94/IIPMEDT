class User:
    def __init__(self):
        self.__user_products = []

    def add_product(self, product: str):
        self.__user_products.append(product)