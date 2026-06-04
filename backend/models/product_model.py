products_db = []

class Product:
    def __init__(self, name, description, price, image_url):
        self.id = len(products_db) + 1
        self.name = name
        self.description = description
        self.price = price
        self.image_url = image_url

    def to_dict(self):
        return self.__dict__